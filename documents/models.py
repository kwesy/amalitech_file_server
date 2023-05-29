from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.crypto import get_random_string
from django.core.validators import FileExtensionValidator



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='document_uploads', validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png']),
        #FileSizeValidator(max_size=10485760)  # 10MB
    ])
    num_downloads = models.PositiveIntegerField(default=0)
    num_emails_sent = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_users = models.ManyToManyField(User, related_name="target_users")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    # allowed_roles = models.ManyToManyField(Group)

    def __str__(self):
        return self.title




