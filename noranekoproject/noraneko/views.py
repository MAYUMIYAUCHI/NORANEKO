from django.shortcuts import render
from django.views import generic
from noraneko.models import NekoPost

# Create your views here.


class NekoPostListView(generic.ListView):
    """投稿したコンテンツの一覧を表示する"""
    model = NekoPost
