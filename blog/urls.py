from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_create/', login_required(views.PostCreate.as_view()), name='post_create'),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),

]