# Generated by Django 2.0 on 2020-03-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='admin',
            field=models.BooleanField(default=True),
        ),
    ]