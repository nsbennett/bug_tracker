# Generated by Django 4.1.6 on 2023-03-17 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0021_alter_ticketclosed_ticket_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketclosed',
            name='ticket_reference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base_app.createticket'),
        ),
    ]