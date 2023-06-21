import os
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .validators import FileSizeValidator



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
    description = models.TextField(max_length=250)
    file = models.FileField(upload_to='document_uploads', validators=[
        FileExtensionValidator(allowed_extensions=['pdf','jpg','jpeg','png','gif','webp','tiff','tif','bmp','svg','doc','docx','xls','xlsx','csv','ppt','pptx','txt','mp4','mov','avi','mkv','wmv','mp3','wav','aac','ogg','ac3','midi']),
        FileSizeValidator(max_size=2**19 * 10)  # 10MB
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
    
    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension




