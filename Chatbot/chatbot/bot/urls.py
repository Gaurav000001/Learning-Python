from django.urls import path
from .views import *

urlpatterns = [
    path('chat/<str:question>', chat_with_gpt, name='chat_with_gpt'),
]