# Generated by Django 4.1.6 on 2023-03-03 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_ticketcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketcomment',
            options={'ordering': ('timestamp',)},
        ),
    ]
