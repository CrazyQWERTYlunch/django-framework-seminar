"""
URL configuration for Seminars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('les1/', include(arg='seminar_app1.urls', namespace='les1')),
    path('les2/', include(arg='seminar_app2.urls', namespace='les2')),
    path('les3/', include(arg='seminar_app3.urls', namespace='les3')),
    path('les4/', include(arg='seminar_app4.urls', namespace='les4')),
    path('les5/', include(arg='seminar_app5.urls', namespace='les5')),
    # path('les6/', include(arg='seminar_app6.urls', namespace='les6')),
    path('__debug__/', include("debug_toolbar.urls")),


]
