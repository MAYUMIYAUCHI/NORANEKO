from django.urls import path
from noraneko.views import NekoPostListView

urlpatterns = [
    path('post-list', NekoPostListView.as_view(), name='post-list'),
]
