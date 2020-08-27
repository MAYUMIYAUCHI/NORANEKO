from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import NekoModel,Replay_chat


# Create your views here.
def indexfunc(repuest):
  return render(repuest,'index.html')

def list_chatfunc(request):
  object_list = NekoModel.objects.all()
  return render(request,'list_chat.html',{'object_list':object_list})

def detail_chatfunc(request,pk):
  object = NekoModel.objects.get(pk=pk)
  return render(request,'detail_chat.html',{'object':object})

class CreateChat(CreateView):
  template_name = 'create_chat.html'
  fields = ('title','content')
  model = NekoModel
  success_url = reverse_lazy('list_chat')

class Replay_chat(CreateView):
    """コメントへの返信作成ビュー。"""
    model = Reply
    form_class = ReplyCreateForm
    template_name = 'create_chat.html'

    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        reply = form.save(commit=False)
        reply.target = comment
        reply.save()
        return redirect('detail_chat', pk=comment.target.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        context['post'] = comment.target
        return context

