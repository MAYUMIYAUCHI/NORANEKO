from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import Create_chat
from django.urls import reverse_lazy
from django.views.generic import CreateView



# Create your views here.
def indexfunc(repuest):
  return render(repuest,'index.html')

def list_chatfunc(request):
  return render(request,'list_chat.html')

def detail_chatfunc(request):
  object = NekoModel.objects.get(pk=pk)
  return render(request,'detail_chat.html',{'object':object})

class Create_chat(CreateView):
  template_name = 'create_chat.html'
  model = Create_chat
  fields = ('title','content')
  succsess_url = reverse_lazy('list_chat')

