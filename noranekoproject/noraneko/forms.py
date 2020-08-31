from django import forms
from noraneko.models import PostComment


class CommentCreateForm(forms.ModelForm):
    """コメント投稿フォーム"""

    class Meta:
        model = PostComment
        exclude = ('target', 'created_at')
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'コメントを入力して下さい。'}
            )
        }