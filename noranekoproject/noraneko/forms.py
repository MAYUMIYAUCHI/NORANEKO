from django import forms
from noraneko.models import PostComment, ReplyComment


class CommentCreateForm(forms.ModelForm):
    """コメント投稿フォーム"""

    class Meta:
        model = PostComment
        # データとしては必要だがユーザが入力してほしくないところ
        exclude = ('target', 'created_at')
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'コメントを入力して下さい。'}
            )
        }

class ReplyCreateForm(forms.ModelForm):
    """コメントに対する返信フォーム"""

    class Meta:
        model = ReplyComment
        exclude = ('target','created_at')

