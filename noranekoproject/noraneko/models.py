from django.db import models
from django.utils import timezone

# 参考サイト：https://blog.narito.ninja/detail/173/


class NekoPostModel (models.Model):
    """掲示板に投稿する内容"""
    name = models.CharField('名前', max_length=255, default='名無し')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class PostComment(models.Model):
    """投稿に紐づくコメント"""
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(
        NekoPostModel, on_delete=models.CASCADE, verbose_name='対象投稿')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]


class ReplyComment(models.Model):
    """コメントに紐づく返信"""
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    target = models.ForeignKey(
        PostComment, on_delete=models.CASCADE, verbose_name='対象コメント')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]
