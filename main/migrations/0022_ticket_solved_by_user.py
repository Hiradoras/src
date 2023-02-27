# Generated by Django 4.1.6 on 2023-02-21 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0021_ticket_solved_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='solved_by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
