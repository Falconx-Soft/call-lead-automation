# Generated by Django 4.1.4 on 2022-12-26 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_admin_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin_emails',
            options={'verbose_name': 'Admin emails', 'verbose_name_plural': 'Admin emails'},
        ),
    ]
