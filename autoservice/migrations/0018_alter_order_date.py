# Generated by Django 5.1.3 on 2024-12-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0017_alter_profilis_nuotrauka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, help_text='Įveskite užsakymo datą', null=True, verbose_name='Data'),
        ),
    ]
