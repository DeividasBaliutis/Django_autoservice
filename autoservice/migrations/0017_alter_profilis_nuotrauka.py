# Generated by Django 5.1.3 on 2024-12-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0016_alter_profilis_nuotrauka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilis',
            name='nuotrauka',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
