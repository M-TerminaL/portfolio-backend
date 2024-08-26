from django.db import models


# Create your models here.

class ContactInformation(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    short_des_one = models.CharField(max_length=300, verbose_name='توضیحات کوتاه اول')
    short_des_two = models.CharField(max_length=300, verbose_name='توضیحات کوتاه دوم')
    location = models.CharField(max_length=100, verbose_name='موقعیت')
    email = models.EmailField(verbose_name='آدرس ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره موبایل')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال',
                                    help_text='فقط یک فرم فعال برای اطلاعات تماس مجاز می باشد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اطلاعات تماس با من'
        verbose_name_plural = 'لیست اطلاعات تماس با من'


class ContactMe(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=400, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن پیام')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'تماس با من'
        verbose_name_plural = 'لیست تماس با من'
