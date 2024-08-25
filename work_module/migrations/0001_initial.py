# Generated by Django 3.2.25 on 2024-08-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('program_language', models.CharField(max_length=200, verbose_name='زبان برنامه')),
                ('video_link', models.URLField(verbose_name='آدرس آی فریم')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'نرم افزار',
                'verbose_name_plural': 'نرم افزارها',
            },
        ),
        migrations.CreateModel(
            name='WebApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('address', models.URLField(verbose_name='آدرس وب اپلیکیشن')),
                ('image', models.ImageField(upload_to='images/web-apps', verbose_name='تصویر صفحه اصلی سایت')),
                ('front_end', models.CharField(max_length=300, verbose_name='تکنولوژی های فرانت')),
                ('back_end', models.CharField(max_length=200, verbose_name='تکنولوژی های بک اند')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'وب اپلیکیشن',
                'verbose_name_plural': 'وب اپلیکیشن ها',
            },
        ),
    ]
