# Generated by Django 4.1.4 on 2022-12-28 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_offers_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_offers',
            name='user',
        ),
    ]
