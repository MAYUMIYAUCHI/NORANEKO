from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import NekoPost,PostComment,ReplyComment
from django.views import generic
from noraneko.forms import CommentCreateForm


# Create your views here.
def indexfunc(repuest):
  return render(repuest,'index')

class NekoPostListView(generic.ListView):
  model = NekoPost
 

class NekoPostDetailView(generic.DetailView):
  model = NekoPost
  

class PostCommentCreateView(generic.CreateView):
  model = PostComment
  form_class = CommentCreateForm

  def form_valid(self,form):
    nekopost = get_object_or_404(NekoPost, pk=self.kwargs['pk'])
    comment = form.save(commit=False)
    comment.target = nekopost
    comment.save()
    return redirect('post_detail',pk=self.kwargs['pk'])
  
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context['nekopost'] = get_object_or_404(NekoPost,pk=self.kwargs['pk'])
    return context
    
class ReplyComment(generic,CreateViwe):
  model = ReplyCreate
  form_class = ReplyCommentForm
  
  def form_valid(self,form):
    comment_pk = self.kwargs['pk']
    comment = get_object_or_404(pk=comment_pk)
    reply = form.save(commit=False)
    reply.target = comment
    reply.save()
    return redirect('post_detail',pk=comment.target.pk)
 

