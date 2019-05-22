from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import MySignUpView, profile, showprofile
from pages import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='index'),
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('profile/', profile, name='profile'),
    path('showprofile/', showprofile, name='showprofile'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
