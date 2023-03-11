from django.db import models
from django.contrib.auth.models import User




class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фамилия' )
    photo = models.ImageField(upload_to='investors', null=True, blank=True, verbose_name='Фото')
    about = models.TextField(verbose_name='Обо мне')
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'
        ordering = ['-id']



class BusinessOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фамилия')    
    photo = models.ImageField(upload_to='business_owners', null=True, blank=True, verbose_name='Фото')
    sphere = models.CharField(max_length=100, null=True, blank=True, verbose_name='Сфера')
    business_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название бизнеса')
    contact_info = models.TextField(null=True, blank=True, verbose_name='Контактная информация')
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = 'Владелец бизнеса'
        verbose_name_plural = 'Владельцы бизнесов'
        ordering = ['-id']




class Business(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE,  verbose_name='Владелец')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма инвестиций')
    conditions = models.IntegerField(verbose_name='Условия')
    term = models.DurationField(verbose_name='Срок окупаемости')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    sphere = models.CharField(max_length=100, null=True, blank=True, verbose_name='Сфера')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Локация')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бизнес'
        verbose_name_plural = 'Бизнесы'
        ordering = ['-id']



class BlockedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Заблокированный пользователь'
        verbose_name_plural = 'Заблокированные пользователи'
        ordering = ['-id']
