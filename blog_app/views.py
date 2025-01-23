from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage
from .forms import CommentForm
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@login_required(login_url='users:login')
def posts_view(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    posts = paginator.get_page(page_number)
    context= {
        'posts':posts,
    }
    return render(request, 'blog/posts.html', context )

@login_required(login_url='users:login')
def post_detail(request,year,month,day,post):
    
    comment_form = CommentForm()
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day = day)
    comments  = post.comments.filter(active=True)
    context = {
        'post':post,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request,'blog/post_detail.html', context)






@method_decorator(login_required(login_url='users:login'), name='dispatch')
class Post_Comment(View):
    def post(self,request):
        form = CommentForm(request.POST)
        post_id = request.POST.get('post_id')
        path_url = request.POST.get('path_url')
        post = get_object_or_404(Post, id=post_id,status=Post.Status.PUBLISHED)
        comment = None
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect(path_url)
    
        
        # return render(request, 'blog/comment.html', {
        #     'post':post,
        #     'form':form,
        #     'comment':comment
        # })