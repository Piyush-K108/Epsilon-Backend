# Generated by Django 4.1.7 on 2023-02-25 12:10

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ProfilePic',
            field=models.ImageField(null=True, upload_to=api.models.student.FileName),
        ),
    ]
