from django.db import models

# Create your models here.

class Certificate(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان گواهی نامه')
    image = models.ImageField(upload_to='images/certificates', verbose_name='تصویر گواهی نامه')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گواهی نامه'
        verbose_name_plural = 'گواهی نامه ها'