from django.urls import path
from . import views

urlpatterns = [
    # doctor side
    path('create/', views.create_blog, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),

    # patient side
    path("blogs/", views.blog_list, name="blog_list"),
    path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
    
    # delete blog
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
