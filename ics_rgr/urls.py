"""ics_rgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from eatcat import views

urlpatterns = [
    path('', views.index),
    path('pets/all', views.pets_list),
    path('pets/<int:pet_id>', views.pet_info),
    path('users/all', views.users_list),
    path('users/<int:pet_id>', views.user_info),
    path('auth', views.auth),
    path('reg', views.registration),
    path('dashboard', views.dashboard),
    path('dashboard/created', views.createdPet),
    path('dashboard/petinfo', views.infoPet),

    path('admin/', admin.site.urls),

]
