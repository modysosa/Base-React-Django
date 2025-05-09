from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage
import json

# Create your views here.
@login_required
def chat_window(request):
    """
    View for the chat window that appears at the bottom right of the page
    """
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat_window.html', {'users': users})

@login_required
def get_messages(request, user_id=None):
    """
    API endpoint to get messages between the current user and another user
    """
    if user_id:
        other_user = get_object_or_404(User, id=user_id)
        messages = ChatMessage.objects.filter(
            (Q(sender=request.user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=request.user))
        ).order_by('timestamp')
        
        # Mark messages as read
        unread_messages = messages.filter(is_read=False, receiver=request.user)
        unread_messages.update(is_read=True)
    else:
        # Get the most recent messages for the current user
        messages = ChatMessage.objects.filter(
            Q(sender=request.user) | Q(receiver=request.user)
        ).order_by('-timestamp')[:20]
    
    message_list = [{
        'id': msg.id,
        'sender': msg.sender.username,
        'sender_id': msg.sender.id,
        'receiver': msg.receiver.username if msg.receiver else None,
        'receiver_id': msg.receiver.id if msg.receiver else None,
        'message': msg.message,
        'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M'),
        'is_read': msg.is_read
    } for msg in messages]
    
    return JsonResponse({'messages': message_list})

@login_required
def send_message(request):
    """
    API endpoint to send a message to another user
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            receiver_id = data.get('receiver_id')
            message_text = data.get('message')
            
            if not message_text:
                return JsonResponse({'status': 'error', 'message': 'Message cannot be empty'}, status=400)
            
            if receiver_id:
                receiver = get_object_or_404(User, id=receiver_id)
            else:
                receiver = None
                
            message = ChatMessage.objects.create(
                sender=request.user,
                receiver=receiver,
                message=message_text
            )
            
            return JsonResponse({
                'status': 'success',
                'message': {
                    'id': message.id,
                    'sender': message.sender.username,
                    'sender_id': message.sender.id,
                    'receiver': message.receiver.username if message.receiver else None,
                    'receiver_id': message.receiver.id if message.receiver else None,
                    'message': message.message,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M'),
                    'is_read': message.is_read
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
def get_users(request):
    """
    API endpoint to get a list of users for the chat
    """
    users = User.objects.exclude(id=request.user.id)
    user_list = [{
        'id': user.id,
        'username': user.username,
        'full_name': f"{user.first_name} {user.last_name}".strip() or user.username,
        # Check if there are unread messages from this user
        'unread': ChatMessage.objects.filter(sender=user, receiver=request.user, is_read=False).exists()
    } for user in users]
    
    return JsonResponse({'users': user_list})
