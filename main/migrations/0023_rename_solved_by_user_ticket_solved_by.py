# Generated by Django 4.1.6 on 2023-02-21 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_ticket_solved_by_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='solved_by_user',
            new_name='solved_by',
        ),
    ]
