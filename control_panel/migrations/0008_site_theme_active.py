# Generated by Django 3.1.1 on 2020-09-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0007_site_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_theme',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]