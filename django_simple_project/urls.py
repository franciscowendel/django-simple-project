"""django_simple_project URL Configuration

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
from django.urls import (
    path,
    include
)
from django.conf.urls.static import static
from django.conf import settings
from django_simple_project.core.urls_3 import router


urlpatterns = [
    # DJANGO ADMIN
    path('admin/', admin.site.urls),

    # CORE URLS
    path('', include('django_simple_project.core.urls')),

    # DJANGO REST FRAMEWORK ADMIN
    path('auth/', include('rest_framework.urls')),

    # API (1) APIView
    path('api/v1/', include('django_simple_project.core.urls_2')),

    # API (2) Generics
    path('api/v2/', include('django_simple_project.core.urls_3')),

    # API (3) Viewsets
    path('api/v3/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
