from .views import home, success
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('success', success, name='success')
]