from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# Create your models here.
class Link(models.Model):
    owner = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="links")
    original_url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=6, unique=True, db_index=True)
    clicks_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null = True, blank=True)
    is_Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.original_url[:10]} -> {self.short_code}"
    
    
    
    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False
    
    def is_Valid(self):
        return self.is_Active and not self.is_expired()