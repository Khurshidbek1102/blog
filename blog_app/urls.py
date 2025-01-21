from django.urls import path
from .views import *
app_name ='blog'
urlpatterns = [
    path('posts/',posts_view, name='posts'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name="post_detail"),
]
