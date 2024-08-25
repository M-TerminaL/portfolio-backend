from django.db import models

# Create your models here.

class WebApplication(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    address = models.URLField(verbose_name='آدرس وب اپلیکیشن')
    image = models.ImageField(upload_to='images/web-apps', verbose_name='تصویر صفحه اصلی سایت')
    front_end = models.CharField(max_length=300, verbose_name='تکنولوژی های فرانت')
    back_end = models.CharField(max_length=200, verbose_name='تکنولوژی های بک اند')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'وب اپلیکیشن'
        verbose_name_plural = 'وب اپلیکیشن ها'


class App(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    program_language = models.CharField(max_length=200, verbose_name='زبان برنامه')
    video_link = models.URLField(verbose_name='آدرس آی فریم')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نرم افزار'
        verbose_name_plural = 'نرم افزارها'