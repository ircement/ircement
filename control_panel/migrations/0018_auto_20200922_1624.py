# Generated by Django 3.1.1 on 2020-09-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0017_auto_20200919_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_news',
            name='description',
            field=models.TextField(),
        ),
    ]
