
from django.urls import path
from .views import indexfunc,list_chatfunc,create_chatfunc,detail_chatfunc

urlpatterns = [
    path('index/',indexfunc, name='index' ),
    path('list_chat/',list_chatfunc, name='list_chat'),
    path('create_chat/',create_chat.as_view(), name='create_chat'),
    path('detail_chat/',detail_chatfunc, name='detail_chat'),

]