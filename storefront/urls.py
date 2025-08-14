# storefront/urls.py
from django.contrib import admin
from django.urls import path, include
from playground import views
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('', views.index),  # Root route loads React
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns