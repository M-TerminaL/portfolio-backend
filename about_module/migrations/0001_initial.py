# Generated by Django 3.2.25 on 2024-08-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_des', models.TextField(verbose_name='درباره من')),
                ('field_of_study', models.CharField(max_length=200, verbose_name='رشته تحصیلی')),
                ('year_of_graduation', models.PositiveIntegerField(verbose_name='سال اخذ مدرک')),
                ('degree', models.CharField(max_length=400, verbose_name='مقطع تحصیلی')),
                ('is_active', models.BooleanField(default=False, help_text='فقط یک درباره من فعال مجاز است', verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'درباره من',
                'verbose_name_plural': 'متن های درباره من',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان مهارت')),
                ('skill_percentage', models.PositiveIntegerField(verbose_name='درصد مهارت')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'مهارت ها',
            },
        ),
    ]
