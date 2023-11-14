from django.urls import path
from .views import experience, experience_new

urlpatterns = [
    path("", experience, name='experience'),
    path("new/", experience_new, name='experience_new')
]