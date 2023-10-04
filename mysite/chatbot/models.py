from django.db import models

# Create your models here.

class Message(models.Model):
    massage_text = models.CharField(max_length=300)
    sent_at = models.DateTimeField('date published', auto_now_add=True)
    is_bot = models.BooleanField(default=False)
    def __str__(self)
        return self.massage_text
    
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self)
        return self.name