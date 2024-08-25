from django.db import models

# Create your models here.

class AboutMe(models.Model):
    about_des = models.TextField(verbose_name='درباره من')
    field_of_study = models.CharField(max_length=200, verbose_name='رشته تحصیلی')
    year_of_graduation = models.PositiveIntegerField(verbose_name='سال اخذ مدرک')
    degree = models.CharField(max_length=400, verbose_name='مقطع تحصیلی')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال',
                                    help_text='فقط یک درباره من فعال مجاز است')

    def __str__(self):
        return f'{self.field_of_study} - {self.year_of_graduation}'

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'متن های درباره من'


class Skill(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مهارت')
    skill_percentage = models.PositiveIntegerField(verbose_name='درصد مهارت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

