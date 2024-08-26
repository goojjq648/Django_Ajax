from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('register/', views.show_register, name='register')
]
