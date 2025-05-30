from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    message = models.TextField(verbose_name='留言内容')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='提交时间')

    def __str__(self):
        return f'{self.name} - {self.created_at}'

# Create your models here.
