from django.contrib.auth.models import User, Group, Permission
from django.db import models

# Create user groups
# group_admin = Group.objects.create(name='Admin')
# group_regular = Group.objects.create(name='Regular User')

# Assign permissions to groups
# permission_upload = Permission.objects.get(codename='add_document')
# permission_download = Permission.objects.get(codename='view_document')
# group_admin.permissions.add(permission_upload, permission_download)
# group_regular.permissions.add(permission_download)

# Assign groups to users
# user1.groups.add(group_admin)
# user2.groups.add(group_regular)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    # Add other fields as per your requirements
    
    def generate_verification_token(self):
        # Implementation remains the same as before
        pass
    
    def __str__(self):
        return self.user.username