# Generated by Django 3.1.1 on 2020-09-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0013_mid_page_b'),
    ]

    operations = [
        migrations.CreateModel(
            name='img_array',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='img_array/img/default/default.png', upload_to='img_array/img/')),
            ],
        ),
    ]