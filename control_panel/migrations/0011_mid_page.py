# Generated by Django 3.1.1 on 2020-09-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0010_auto_20200914_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='mid_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='mid_page/img/default/default.png', upload_to='mid_page/img/')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('counter', models.TextField()),
            ],
        ),
    ]
