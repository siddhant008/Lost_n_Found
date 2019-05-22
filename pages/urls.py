from django.urls import path
from .views import *


app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('contact_us/', contact, name='contact_us'),
    path('about_us/', about, name="about_us"),
]

