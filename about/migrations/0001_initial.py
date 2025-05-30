# Generated by Django 3.1.4 on 2025-05-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='宠物名称')),
                ('age', models.PositiveIntegerField(verbose_name='年龄（月）')),
                ('breed', models.CharField(max_length=50, verbose_name='品种')),
                ('description', models.TextField(verbose_name='简介')),
                ('image', models.ImageField(upload_to='pets/', verbose_name='宠物照片')),
            ],
        ),
    ]
