from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from noraneko.models import NekoPost, PostComment
from noraneko.forms import CommentCreateForm

# Create your views here.


class NekoPostListView(generic.ListView):
    """投稿したコンテンツの一覧を表示する"""
    model = NekoPost


class NekoPostDetailView(generic.DetailView):
    """投稿したコンテンツの詳細を表示する"""
    model = NekoPost


class PostCommentCreateView(generic.CreateView):
    """投稿したコンテンツのコメントを作成する"""
    model = PostComment
    form_class = CommentCreateForm

    def form_valid(self, form):
        """データがPOSTされる時に呼ばれるメソッド"""
        print(self.kwargs['pk'])
        nekopost_pk = self.kwargs['pk']
        nekopost = get_object_or_404(NekoPost, pk=nekopost_pk)
        comment = form.save(commit=False)
        comment.target = nekopost
        comment.save()
        return redirect('post_detail', pk=nekopost_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nekopost'] = get_object_or_404(NekoPost, pk=self.kwargs['pk'])
        return context
