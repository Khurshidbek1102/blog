from django.contrib import admin
from django.urls import path, include
from .views import homePage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name='homepage'),
    path('blogs/', include('blog_app.urls')),
    path('users/', include('users.urls')),
]
