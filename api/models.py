from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    choices_durum = [('üye', 'Üye'), ('isveren', 'İşveren')]
    durum = models.CharField(choices=choices_durum, max_length=50)
    foto = models.FileField(upload_to='user_image', verbose_name='Fotoğraf', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Kullanıcılar'