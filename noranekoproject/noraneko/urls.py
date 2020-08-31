from django.urls import path
from noraneko.views import NekoPostListView, NekoPostDetailView, PostCommentCreateView

urlpatterns = [
    path('post-list', NekoPostListView.as_view(), name='post_list'),
    path('post-list/<int:pk>/', NekoPostDetailView.as_view(), name='post_detail'),
    path('comment-create/<int:pk>/',
         PostCommentCreateView.as_view(), name='comment_create'),
]
