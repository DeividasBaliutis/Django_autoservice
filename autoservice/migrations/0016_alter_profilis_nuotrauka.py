# Generated by Django 5.1.3 on 2024-12-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0015_alter_profilis_nuotrauka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilis',
            name='nuotrauka',
            field=models.ImageField(default='autoservice/media/profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]