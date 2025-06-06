# Generated by Django 3.1.4 on 2025-05-29 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('message', models.TextField(verbose_name='留言内容')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
            ],
        ),
    ]
