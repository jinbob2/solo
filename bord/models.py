from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .fields import ThumbnailImageField


# Create your models here.
class Bord(models.Model):
    check = models.IntegerField(default=0)  # 같은 형식의 게시판 갯수 여러개만들기
    title = models.CharField(max_length=120)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('photo Description', blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)
    embed_code = models.TextField()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bord:detail', args=(self.id,))
# Create your models here.

