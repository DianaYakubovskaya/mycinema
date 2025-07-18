# Generated by Django 5.1.1 on 2024-10-20 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_remove_show_available_seats_remove_show_hall_number_and_more'),
        ('tickets', '0005_alter_ticket_ticket_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.show'),
        ),
    ]
