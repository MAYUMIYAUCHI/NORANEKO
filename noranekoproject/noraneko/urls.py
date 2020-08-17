
from django.urls import path
from .views import indexfunc,list_chatfunc

urlpatterns = [
    path('index/',indexfunc ),
    path('list_chat/',list_chatfunc),

]