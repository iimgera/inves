from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    """
    Моделька для категории, обьявлений.
    """
    title = models.CharField(
        max_length=150, verbose_name='Наименнование сферы бизнеса'
    )

    class Meta:
        verbose_name_plural = 'Категории Объявлений'
        verbose_name = 'Категория объявлений'

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    """
    Моделька объявлений
    """

    name = models.CharField(
        max_length=255, verbose_name='Название компании',
        null=False, help_text='Название Компании', blank=False
    )
    description = RichTextUploadingField(
        verbose_name='Описание компании, и на что нужно инвестиции', null=False,
        help_text='Описание компании', blank=False
    )
    image = models.ImageField(
        null=False, blank=False, help_text='Лого компании', verbose_name='Логотип компании'
    )
    category = models.ForeignKey(
        Category, null=False, on_delete=models.RESTRICT
    )