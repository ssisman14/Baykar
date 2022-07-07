from django.contrib import admin
from api.models import User
from django.utils.html import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_img', 'first_name', 'last_name', 'email', 'durum')

    def get_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.foto}" width="50" height="50" />')

    get_img.short_description = 'RESİM'
