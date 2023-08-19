from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('menu', menu, name='menu'),
    path('add-dish', add_dish, name='add_dish'),
    path('delete-dish/<int:dishID>', delete_dish, name='delete_dish'),
    path('update-availability/<int:dishID>/<str:is_available>', update_availability, name='update_availability'),
    path('update-dish/<int:dishID>', update_dish, name='update_dish'),
    path('order-items', order_items, name='order_items'),
    path('orders', orders, name='orders'),
    path('order-details/<int:orderID>', order_details, name='order_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()