from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),

]