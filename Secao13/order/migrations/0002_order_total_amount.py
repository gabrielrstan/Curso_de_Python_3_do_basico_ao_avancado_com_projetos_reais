# Generated by Django 5.0.4 on 2024-04-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
