# Generated by Django 4.1.7 on 2023-03-11 18:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('image', models.ImageField(help_text='Логотип', upload_to='', verbose_name='Логотип')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма инвестиций')),
                ('term', models.DurationField(verbose_name='Срок окупаемости')),
                ('description', ckeditor.fields.RichTextField(help_text='Описание Объявления', verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный ли пользователь')),
                ('is_premium', models.BooleanField(default=False, verbose_name='Премиум объявление')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Локация(Город страна)')),
                ('created_at', models.DateField(auto_now_add=True, help_text='Дата создания поста', verbose_name='Дата создания поста')),
            ],
            options={
                'verbose_name': 'Бизнес',
                'verbose_name_plural': 'Бизнесы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Введите ваш текст', help_text='Название Категории', max_length=255, verbose_name='Название Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='BusinessDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Моделька для Бизнес Плана и так далее')),
                ('contact', models.CharField(blank=True, help_text='Контакт для связи', max_length=255, null=True, verbose_name='Контакт для связи')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business', verbose_name='Бизнес от которого он наследуется')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.RESTRICT, to='business.category', verbose_name='Сфера деятельности'),
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.businessowner', verbose_name='Владелец'),
        ),
    ]
