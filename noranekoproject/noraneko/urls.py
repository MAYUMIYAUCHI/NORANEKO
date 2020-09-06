
from django.urls import path
from .views import indexfunc,list_chatfunc,detail_chatfunc,CreateChat,Reply_Chat_views


urlpatterns = [
    path('index/',indexfunc, name='index' ),
    path('list_chat/',list_chatfunc, name='list_chat'),
    path('create_chat/',CreateChat.as_view(), name='create_chat'),
    path('detail_chat/<int:pk>',detail_chatfunc, name='detail_chat'),
    path('reply_chat/<int:pk>',Reply_Chat_views.as_view(), name='reply_chat')

]