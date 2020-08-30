from django.contrib import admin
from noraneko import models

# 参考サイト：https://blog.narito.ninja/detail/173/


class ReplyCommentInline(admin.StackedInline):
    model = models.ReplyComment
    extra = 5


class PostCommentAdmin(admin.ModelAdmin):
    inlines = [ReplyCommentInline]


# Register your models here.
admin.site.register(models.NekoPostModel)
admin.site.register(models.PostComment, PostCommentAdmin)
admin.site.register(models.ReplyComment)
