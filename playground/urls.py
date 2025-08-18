from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
]


