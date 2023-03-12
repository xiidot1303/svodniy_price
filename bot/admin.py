from django.contrib import admin
from bot.models import *
from django.utils.html import format_html

class Bot_userAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'phone', 'date']
    search_fields = ['name', 'username', 'phone']
    list_filter = ['date']
    list_display_links = None

class MesageAdmin(admin.ModelAdmin):
    list_display = ['bot_users_name', 'small_text', 'open_photo', 'open_video', 'open_file', 'date']
    list_display_links = None
    fieldsets = (
        ('', {
            'fields': ['bot_users', 'text', 'photo', 'video', 'file'],
            'description': 'Выберите пользователей, которым вы хотите отправить сообщение, или просто оставьте поле пустым, чтобы отправить всем пользователям.', 
        }),

    )
    
    def bot_users_name(self, obj):
        result = ''
        if users:=obj.bot_users.all():
            for user in users:
                result += f'{user.name} {user.phone} | '
        else:
            result = 'Все'
        return result
    bot_users_name.short_description = 'Пользователи бота'

    def small_text(self, obj):
        cut_text = obj.text[:20] + ' ...' if len(obj.text) >= 20 else obj.text
        return format_html(f'<p title={obj.text}>{cut_text}</p>')

    def open_photo(self, obj):
        if obj.photo:
            change_url = f'/files/{obj.photo}'
            return format_html('<a target="_blank" class="btn btn-success" href="{}"><i class="fas fa-eye"></i> Открыть</a>', change_url)
        return None
    open_photo.short_description = 'Фото'

    def open_video(self, obj):
        if obj.video:
            change_url = f'/files/{obj.video}'
            return format_html('<a target="_blank" class="btn btn-warning" href="{}"><i class="fas fa-eye"></i> Открыть</a>', change_url)
        return None
    open_video.short_description = 'Видео'

    def open_file(self, obj):
        if obj.file:
            change_url = f'/files/{obj.file}'
            return format_html('<a target="_blank" class="btn btn-primary" href="{}"><i class="fas fa-eye"></i> Открыть</a>', change_url)
        return None
    open_file.short_description = 'Файл'

    def get_form(self, request, obj=None, **kwargs):
        form = super(MesageAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['bot_users'].widget.attrs['style'] = 'width: 20em;'
        return form

admin.site.register(Bot_user, Bot_userAdmin)
admin.site.register(Message, MesageAdmin)