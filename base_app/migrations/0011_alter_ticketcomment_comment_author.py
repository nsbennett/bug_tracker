# Generated by Django 4.1.6 on 2023-03-14 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('base_app', '0010_alter_createticket_ticket_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcomment',
            name='comment_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
