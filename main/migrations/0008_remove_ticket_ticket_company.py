# Generated by Django 4.1.6 on 2023-02-14 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_profile_delete_customers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_company',
        ),
    ]