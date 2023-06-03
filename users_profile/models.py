from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)

    
    def generate_verification_token(self):
        token = get_random_string(length=20)
        self.verification_token = token
        self.save()
    
    def __str__(self):
        return self.user.username