from django.db import models
from django.contrib.auth.models import User
from django.utils  import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)
    
    
class Post(models.Model):
    
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFT = "DF", 'Draft'
        
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]
        
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year,
                                                  self.publish.month,
                                                  self.publish.day,
                                                  self.slug])
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            related_name='comments')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
    
    def __str__(self):
        return f"Comment by {self.user} on {self.post}"