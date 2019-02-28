from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
   
)
from . import views
from django.conf.urls import url

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('', views.alter, name='blog-alter'),
    path('test/', views.test, name='blog-test'),
    path('parallax/', views.parallax, name='blog-parallax'),
    path('like/', views.LikePost, name='like_post'),
    path('corpseAI/', views.ChatterBotAppView.as_view(), name='main'),
    path('api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),
    
]