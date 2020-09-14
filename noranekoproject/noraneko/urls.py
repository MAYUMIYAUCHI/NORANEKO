
from django.urls import path
from .views import NekoPostListView,NekoPostDetailView,PostCommentCreateView,ReplyCommentView


urlpatterns = [
    path('post_list/',NekoPostListView.as_view(), name='post_list'),
    path('post_list/<int:pk>/',NekoPostDetailView.as_view(), name='post_detail'),
    path('comment_create/<int:pk>',PostCommentCreateView.as_view(), name='comment_create'),
    path('reply_comment/<int:pk>', ReplyCommentView.as_view(), name='reply_comment'),
   

]