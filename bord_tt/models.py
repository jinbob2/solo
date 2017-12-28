from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .fields import ThumbnailImageField


# Create your models here.
class Bord(models.Model):
    check = models.IntegerField(default=0)  # 같은 형식의 게시판 갯수 여러개만들기
    title = models.CharField(max_length=120) # 타이틀
    image = ThumbnailImageField(upload_to='bord/%Y/%m') # 이미지 넣는거고
    description = models.TextField('bord Description', blank=True) #설명 넣는것
    timestamp = models.DateTimeField(auto_now=True) # 생성 시간 표시
    updated = models.DateTimeField(auto_now=True) # 업데이트 시간 표시
    user = models.ForeignKey(User, null=True) # 유저 네임
    embed_code = models.TextField(null=True)# 기존값 # 비디오 코드

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bord:detail', args=(self.id,))
# Create your models here.

