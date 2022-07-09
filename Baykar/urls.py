"""Baykar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from webHMTL.views import *
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'related_company_user', RelatedCompanyUserViewSet)
router.register(r'school',SchoolViewSet)
router.register(r'related_school_user', RelatedUserSchoolViewSet)
router.register(r'yetenek',YetenekViewSet)
router.register(r'aday_deneyimleri', AdayDeneyimleriViewSet),
router.register(r'aday', AdayViewSet)
router.register(r'related_aday_yetenek', RelatedAdayYetenekViewSet)
router.register(r'related_aday_kullanici', RelatedAdayKullaniciViewSet)
router.register(r'related_aday_ilan', RelatedUserIlanViewSet)
router.register(r'ilan', IlanViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('', app, name='app'),
                  path('user_login/', user_login, name='user_login'),
                  path('user_sing_in/', user_sing_in, name='user_sing_in'),
                  path('logout/', logout_user, name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
