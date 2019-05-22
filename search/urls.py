from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from .views import search, advanced_search, all_search


app_name = 'search'

urlpatterns = [
    path('', search, name='search'),
    path('advanced_search/', advanced_search, name='advanced_search'),
    path('all_search/', all_search, name='all_search'),
    # path('print_result/', print_result, name='print_result'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
