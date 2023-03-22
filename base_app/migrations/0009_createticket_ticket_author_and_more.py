# Generated by Django 4.1.6 on 2023-03-14 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_app', '0008_rename_ticket_id_ticketcomment_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='createticket',
            name='ticket_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketcomment',
            name='comment_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]