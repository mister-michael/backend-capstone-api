"""projectmapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from backendapi.views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'equipmenttypes', EquipmentTypes, 'equipmenttype')
router.register(r'batterytypes', BatteryTypes, 'batterytype')
router.register(r'clients', Clients, 'client')
router.register(r'equipments', Equipments, 'equipment')
router.register(r'employees', Employees, 'employee')
router.register(r'users', Users, 'user')
router.register(r'photoshoots', Photoshoots, 'photoshoot')
router.register(r'photoshootequipments', PhotoshootEquipments, 'photoshootequipment')
router.register(r'photoshootnotes', PhotoshootNotes, 'photoshootnote')
router.register(r'clientnotes', ClientNotes, 'clientnote')
router.register(r'photoshootstaffs', PhotoshootStaffs, 'photoshootstaff')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)