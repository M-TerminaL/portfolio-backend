from django.db import models


# Create your models here.

class ProfileSetting(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    img_profile = models.ImageField(upload_to='images/profile', verbose_name='تصویر پروفایل')
    bio_one = models.CharField(max_length=200, verbose_name='بیوگرافی اول')
    bio_two = models.CharField(max_length=200, verbose_name='بیوگرافی دوم')
    resume = models.FileField(upload_to='files/resume', verbose_name='فایل رزومه')
    github = models.URLField(verbose_name='لینک گیت هاب')
    instagram = models.CharField(max_length=200, verbose_name='آی دی اینستاگرام')
    telegram = models.CharField(max_length=200, verbose_name='آی دی تلگرام')
    whatsapp = models.CharField(max_length=200, verbose_name='شماره واتس آپ')
    is_main_profile = models.BooleanField(default=False, verbose_name='پروفایل اصلی',
                                          help_text='فقط یک پروفایل مجاز به استفاده می باشد', db_index=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'
