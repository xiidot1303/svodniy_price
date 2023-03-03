from django.db import models

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'uz'), (1, 'ru'), (2, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)

class Drug(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    title_en = models.CharField(null=True, blank=True, max_length=255)
    term = models.CharField(null=True, blank=True, max_length=32) # срок
    price = models.CharField(null=True, blank=True, max_length=64)
    provider_name = models.CharField(null=True, blank=True, max_length=255)
    manufacturer = models.CharField(null=True, blank=True, max_length=255)
    country = models.CharField(null=True, blank=True, max_length=64)
    published = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True)

    @property
    def provider(self):
        name = self.provider_name.replace(' - ', '-')
        filter = Provider.objects.filter(name__contains = name.lower())
        return filter[0] if filter else None

class Provider(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    phone = models.CharField(null=True, blank=True, max_length=255)
    address = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self) -> str:
        return self.name