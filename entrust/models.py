from django.db import models
from django.utils import timezone

class EntrustApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '已通过'),
        ('rejected', '已拒绝'),
    )

    name = models.CharField(max_length=100, verbose_name='姓名')
    phone = models.CharField(max_length=20, verbose_name='联系电话')
    pet_name = models.CharField(max_length=50, verbose_name='宠物名称')
    pet_age = models.PositiveIntegerField(verbose_name='宠物年龄')
    pet_species = models.CharField(max_length=50, verbose_name='宠物品种')
    description = models.TextField(verbose_name='宠物描述')
    pet_image = models.ImageField(upload_to='entrust_pets/', verbose_name='宠物图片')
    application_time = models.DateTimeField(default=timezone.now, verbose_name='申请时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='审核状态')

    def __str__(self):
        return f'{self.name}的{self.pet_name}寄养申请'
