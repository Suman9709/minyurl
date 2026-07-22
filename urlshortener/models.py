from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Link(models.Model):
    owner = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="links")
    original_url = models.CharField()
    short_code = models.CharField(max_length=6, unique=True, db_index=True)
    clicks_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null = True, blank=True)
    is_Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.original_url[:10]} -> {self.short_code}"
    
    