from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import NekoModel,Reply_Chat
from .forms import ReplyCreateForm 


# Create your views here.
def indexfunc(repuest):
  return render(repuest,'index')

def list_chatfunc(request):
  object_list = NekoModel.objects.all()
  return render(request,'list_chat',{'object_list':object_list})

def detail_chatfunc(request,pk):
  object = NekoModel.objects.get(pk=pk)
  return render(request,'detail_chat',{'object':object})

class CreateChat(CreateView):
  template_name = 'create_chat'
  fields = ('title','content')
  model = NekoModel
  success_url = reverse_lazy('list_chat')

class Reply_Chat_views(CreateView):
    """コメントへの返信作成ビュー。"""
    model = Reply_Chat
    form_class = ReplyCreateForm
    template_name = 'create_chat'

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(NekoModel, pk=post_pk)
        reply = form.save(commit=False)
        reply.target = post
        reply.save()
        return redirect('detail_chat', pk=post_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(NekoModel, pk=self.kwargs['pk'])
        return context


