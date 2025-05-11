from django.db import models

class User(models.Model):
    # username = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    # email = models.EmailField(unique=True, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    