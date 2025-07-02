from django.db import models
from zoneinfo import ZoneInfo





class AccessCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    expires_at = models.DateTimeField()
    
    def is_valid(self):
        from django.utils import timezone
        now = timezone.now().astimezone(ZoneInfo("America/Edmonton"))
        return now <= self.expires_at
    