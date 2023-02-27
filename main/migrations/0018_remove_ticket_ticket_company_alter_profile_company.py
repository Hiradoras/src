# Generated by Django 4.1.6 on 2023-02-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_ticket_ticket_company_alter_profile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_company',
        ),
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(choices=[('SUP', 'Support'), ('KTN', 'Koton'), ('LCW', 'LcWaikiki'), ('DFC', 'DeFacto'), ('CLS', "Colin's")], max_length=3),
        ),
    ]
