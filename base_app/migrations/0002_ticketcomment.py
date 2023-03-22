# Generated by Django 4.1.6 on 2023-03-03 03:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.createticket')),
            ],
        ),
    ]
