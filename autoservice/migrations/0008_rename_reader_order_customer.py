# Generated by Django 5.1.3 on 2024-12-05 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0007_order_reader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='reader',
            new_name='customer',
        ),
    ]
