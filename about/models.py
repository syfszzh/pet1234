from django.db import models

class Pet(models.Model):
    name = models.CharField('宠物名称', max_length=100)
    age = models.PositiveIntegerField('年龄（月）')
    breed = models.CharField('品种', max_length=50)
    description = models.TextField('简介')
    image = models.ImageField('宠物照片', upload_to='pets/')

    def __str__(self):
        return self.name


from django.utils import timezone


class AdoptionApplication(models.Model):
    PET_STATUS = [('pending','待审核'),('approved','已通过'),('rejected','已拒绝')]
    pet = models.ForeignKey('entrust.EntrustApplication', on_delete=models.CASCADE, verbose_name='关联宠物')  # 指定EntrustApplication属于entrust应用
    applicant_name = models.CharField('申请人姓名', max_length=50)
    applicant_phone = models.CharField('联系电话', max_length=20)
    applicant_address = models.CharField('居住地址', max_length=200)
    apply_time = models.DateTimeField('申请时间', default=timezone.now)
    status = models.CharField('审核状态', max_length=20, choices=PET_STATUS, default='pending')

    def __str__(self):
        return f'{self.applicant_name}申请领养{self.pet.pet_name}'


class CorporatePet(models.Model):
    name = models.CharField('工作犬名称', max_length=100)
    age = models.PositiveIntegerField('年龄（月）')
    breed = models.CharField('品种', max_length=50)
    work_type = models.CharField('工作类型', max_length=50, help_text='如导盲犬、搜救犬等')
    training_status = models.CharField('训练状态', max_length=50, choices=[('in_progress','训练中'),('qualified','已认证')])
    description = models.TextField('工作能力简介')
    image = models.ImageField('工作犬照片', upload_to='corporate_pets/')

    def __str__(self):
        return self.name
