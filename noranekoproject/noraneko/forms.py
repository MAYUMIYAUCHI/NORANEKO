from django import forms
from .models import Reply_Chat

class ReplyCreateForm(forms.ModelForm):

    """返信コメント投稿フォーム"""

    class Meta:
        model = Reply_Chat
        fields = ('name','text')
        exclude = ('good',)
        labels = {
          'name':'名前',
          'text':'コメント'
        }
        help_texts = {
            'name': '名前を入力',
            'text': 'コメントを入力'
        }