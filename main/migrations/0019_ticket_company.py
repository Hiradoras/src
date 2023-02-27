# Generated by Django 4.1.6 on 2023-02-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_ticket_ticket_company_alter_profile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='company',
            field=models.CharField(blank=True, choices=[('SUP', 'Support'), ('KTN', 'Koton'), ('LCW', 'LcWaikiki'), ('DFC', 'DeFacto'), ('CLS', "Colin's")], max_length=3),
        ),
    ]