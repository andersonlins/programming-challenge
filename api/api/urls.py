"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from modules.title import viewsets

production_router = DefaultRouter()
production_router.register(r'type', viewset=viewsets.TypeViewSet)
production_router.register(r'genre', viewset=viewsets.GenreViewSet)
production_router.register(r'title', viewset=viewsets.TitleViewSet)
production_router.register(r'rating', viewset=viewsets.RatingViewSet)
production_router.register(r'profession', viewset=viewsets.ProfessionViewSet)
production_router.register(r'person', viewset=viewsets.PersonViewSet)


urlpatterns = [
    url(r'^$', lambda request: redirect(reverse('api-root'))),

    url(r'^api/titles/', include(production_router.urls), name='api-root'),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
