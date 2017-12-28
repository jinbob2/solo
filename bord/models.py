from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Bord(models.Model):
    check = models.IntegerField(default=0)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='bord/%Y/%m')
    description = models.TextField('Bord Description', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)
    embed_code = models.TextField(null=True)  # 기존값 # 비디오 코드

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bord:detail', args=(self.id,))