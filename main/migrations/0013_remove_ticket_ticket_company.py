# Generated by Django 4.1.6 on 2023-02-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_profile_company_alter_ticket_ticket_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_company',
        ),
    ]
