from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    choices_durum = [('üye', 'Üye'), ('isveren', 'İşveren')]
    durum = models.CharField(choices=choices_durum, max_length=50)
    foto = models.FileField(upload_to='user_image', verbose_name='Fotoğraf', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Kullanıcılar'


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='İsim')
    img = models.FileField(upload_to='sirket', verbose_name='Resim', blank=True, null=True)
    desc = models.CharField(max_length=350, verbose_name='Açıklama')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Şirketler'


class RelatedCompanyUser(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Şirket")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Kullnıcı")

    class Meta:
        verbose_name_plural = "Şirket/Kullanıcı İlişkileri"


class School(models.Model):
    name = models.CharField(max_length=80, verbose_name="İsim")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Okullar"


class RelatedUserSchool(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.PROTECT)
    school = models.ForeignKey(School, verbose_name="Okul", on_delete=models.PROTECT)
    department = models.CharField(max_length=50, verbose_name="Bölüm")
    start = models.DateField(verbose_name="Başlangıç")
    end = models.DateField(verbose_name="Bitiş")

    class Meta:
        verbose_name_plural = "Kullanıcı/Okul İlişkileri"


class Yetenekler(models. Model):
    name = models.CharField(max_length=60, verbose_name="İsim")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Yetenekler"


class AdayDeneyimler(models.Model):
    user = models.ForeignKey(User, verbose_name='Kullanıcı', on_delete=models.PROTECT)
    sirket = models.CharField(max_length=100,  verbose_name='sirket')
    gorev = models.CharField(max_length=120, verbose_name='görev')
    start = models.DateField(verbose_name="Başlangıç")
    end = models.DateField(verbose_name="Bitiş", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Aday Deneyimleri"


class AdayBilgileri(models.Model):
    name = models.CharField(max_length=60, verbose_name="Başlık")
    summary = models.CharField(max_length=1000, verbose_name="Özet")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Aday Bilgileri"


class RelatedAdayYetenek(models.Model):
    aday = models.ForeignKey(AdayBilgileri, verbose_name="Aday", on_delete=models.PROTECT)
    yetenek = models.ForeignKey(Yetenekler, verbose_name="Yetenek", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Aday Yetenek İlişkileri"


class RelatedAdayKullanici(models.Model):
    aday = models.ForeignKey(AdayBilgileri, verbose_name='Aday', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='kullanıcı', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Aday Kullanıcı İlişkileri"


class Ilan(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Şirket')
    date = models.DateField(verbose_name="İlan Tarihi")
    yayinlayan = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="yayınlayan")
    type = models.CharField(max_length=30, verbose_name="Çalışma Tipi")
    city = models.CharField(max_length=60, verbose_name="Şehir")
    description = models.TextField(verbose_name="Açıklama")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "İlanlar"


class RelatedIlanKullanici(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.PROTECT)
    ilan = models.ForeignKey(Ilan, verbose_name="İlan", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Kullanıcı İlan İlişkileri"