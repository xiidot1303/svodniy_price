from django.db import models
from datetime import datetime

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'uz'), (1, 'ru'), (2, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)

class Drug(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, verbose_name='Торговое название')
    title_en = models.CharField(null=True, blank=True, max_length=255, verbose_name='Международное название')
    term = models.CharField(null=True, blank=True, max_length=32, verbose_name='Срок годности')
    price = models.CharField(null=True, blank=True, max_length=64, verbose_name='Цена сум')
    provider_name = models.CharField(null=True, blank=True, max_length=255, verbose_name='Поставщик')
    manufacturer = models.CharField(null=True, blank=True, max_length=255, verbose_name='Производитель')
    country = models.CharField(null=True, blank=True, max_length=64, verbose_name='Страна')
    published = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True, verbose_name='Дата загрузки')

    def save(self, *args, **kwargs):
        self.published = datetime.now()
        return super(Drug, self).save(*args, **kwargs)

    @property
    def provider(self):
        name = self.provider_name.replace(' - ', '-')
        filter = Provider.objects.filter(name__contains = name.lower())
        return filter[0] if filter else None

    class Meta:
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарство"

class Provider(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='Имя')
    phone = models.CharField(null=True, blank=True, max_length=255, verbose_name='Телефон')
    address = models.CharField(null=True, blank=True, max_length=255, verbose_name='Адрес')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

class Info(models.Model):
    about_uz = models.TextField(null=True, blank=False, max_length=1024, verbose_name='О нас (UZ)')
    about_ru = models.TextField(null=True, blank=False, max_length=1024, verbose_name='О нас (РУ)')
    partners = models.FileField(null=True, blank=False, upload_to="info/", verbose_name='Партнеры')
    site = models.CharField(null=True, blank=False, max_length=64, verbose_name='Сайт')

    class Meta:
        verbose_name = "Инфо"
        verbose_name_plural = "Инфо"

class Excel(models.Model):
    file = models.FileField(null=True, blank=False, upload_to="excel/", verbose_name='Файл')
    published = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True, verbose_name='Дата загрузки')
    is_uploaded = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.published = datetime.now()
        return super(Excel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Эксель"
        verbose_name_plural = "Эксель"