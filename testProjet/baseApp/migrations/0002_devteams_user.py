# Generated by Django 5.0.1 on 2024-01-21 21:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devteams',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]