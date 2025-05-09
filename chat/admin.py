from django.contrib import admin
from .models import ChatMessage

# Register your models here.
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp', 'sender', 'receiver')
    search_fields = ('message', 'sender__username', 'receiver__username')
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)
