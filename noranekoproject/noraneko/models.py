from django.db import models


# Create your models here.
class NekoModel (models.Model):
  name = models.CharField('名前', max_length=255, default='名無し')
  title = models.CharField(max_length=100)
  content = models.TextField()
  good = models.IntegerField(null=True, blank=True, default=0)


  def __str__(self):
        return self.title


class Reply_Chat(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('本文')
    good = models.IntegerField(null=True, blank=True, default=0)
 

    def __str__(self):
        return self.text[:20]