from django.contrib import admin
from api.models import User, Company, RelatedCompanyUser, School, RelatedUserSchool, \
    Yetenekler,  AdayDeneyimler, AdayBilgileri, RelatedAdayYetenek, Ilan, \
    RelatedAdayKullanici, RelatedIlanKullanici

from django.utils.html import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_img', 'first_name', 'last_name', 'email', 'durum')

    def get_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.foto}" width="50" height="50" />')

    get_img.short_description = 'RESİM'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_img', 'desc')

    def get_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="50" height="50" />')

    get_img.short_description = 'RESİM'


@admin.register(RelatedCompanyUser)
class RelCompanyUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(RelatedUserSchool)
class RelUserSchoolAdmin(admin.ModelAdmin):
    list_display = ('school', 'user',)


@admin.register(Yetenekler)
class YeteneklerAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(AdayDeneyimler)
class AdayDeneyimleriAdmin(admin.ModelAdmin):
    list_display = ('user', 'sirket', 'gorev', 'start', 'end')


@admin.register(AdayBilgileri)
class AdayBilgileriAdmin(admin.ModelAdmin):
    list_display = ('name', 'summary',)


@admin.register(RelatedAdayYetenek)
class RelatedAdayYetenekAdmin(admin.ModelAdmin):
    list_display = ('aday', 'yetenek',)


@admin.register(RelatedAdayKullanici)
class RelatedAdayKullaniciAdmin(admin.ModelAdmin):
    list_display = ('aday', 'user',)


@admin.register(Ilan)
class IlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'date', 'yayinlayan')


@admin.register(RelatedIlanKullanici)
class RelatedIlanKullaniciAdmin(admin.ModelAdmin):
    list_display = ('user', 'ilan',)