# Generated by Django 5.0.3 on 2024-03-12 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crew',
            old_name='member_id',
            new_name='master',
        ),
    ]
