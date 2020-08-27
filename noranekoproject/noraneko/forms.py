from .models import Reply_Chat

class ReplyCreateForm(Replay_Chat):
    """返信コメント投稿フォーム"""

    class Meta:
        model = replay_chat
        exclude = ('target', 'created_at')
        widgets = {
            'text': Textarea(
                attrs={
                  'コメント'
                }
            )
        }