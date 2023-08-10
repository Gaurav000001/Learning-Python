from django.urls import path
from . import views

urlpatterns = [
    path('display_menu/', views.display_menu, name='display_menu'),
    path('remove_dish/<str:dish_id>/', views.remove_dish, name='remove_dish'),
    path('update_availability/', views.update_availability, name='update_availability'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('take_order/', views.take_order, name='take_order'),
    path('update_order_status/<str:order_id>/', views.update_order_status, name='update_order_status'),
    path('review_orders/', views.review_orders, name='review_orders'),
]
