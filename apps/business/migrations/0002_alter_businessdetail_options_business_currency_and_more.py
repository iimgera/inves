# Generated by Django 4.1.7 on 2023-03-11 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessdetail',
            options={'verbose_name': 'Бизнес Деталь', 'verbose_name_plural': 'Бизнес Детали'},
        ),
        migrations.AddField(
            model_name='business',
            name='currency',
            field=models.CharField(default=1, help_text='Валюта', max_length=20, verbose_name='Валюта не успел сделать Choices'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Категории', max_length=100, null=True, on_delete=django.db.models.deletion.RESTRICT, to='business.category', verbose_name='Сфера деятельности'),
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(help_text='Описание Объявления', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='business',
            name='term',
            field=models.CharField(help_text='Срок за сколько окупится проект', max_length=255, verbose_name='Срок окупаемости'),
        ),
    ]