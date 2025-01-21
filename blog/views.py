from django.shortcuts import render
from blog_app.models import Post
def homePage(request):
    
    return render(request, 'index.html' )