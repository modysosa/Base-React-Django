from django.urls import path
from . import views

urlpatterns = [
    path('window/', views.chat_window, name='chat_window'),
    path('messages/<int:user_id>/', views.get_messages, name='get_messages_with_user'),
    path('messages/', views.get_messages, name='get_messages'),
    path('send/', views.send_message, name='send_message'),
    path('users/', views.get_users, name='get_users'),
]
