# Generated by Django 3.1.1 on 2023-03-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0013_alter_createticket_ticket_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketClosed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_status', models.CharField(choices=[('Open ticket', 'Open ticket'), ('Under review', 'Under review'), ('Closed', 'Closed')], default='Open ticket', max_length=100, verbose_name='Ticket Status')),
            ],
        ),
    ]