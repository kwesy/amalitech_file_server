# Generated by Django 4.1 on 2023-06-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_remove_document_allowed_roles_document_target_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]