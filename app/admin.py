from django.contrib import admin
from app.models import *
from app.forms import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class DrugAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_en', 'price', 'provider_name', 'published']
    search_fields = ['title']

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address']

admin.site.register(Language, LanguageAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Provider, ProviderAdmin)
