# Generated by Django 3.1.1 on 2020-09-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0002_auto_20200903_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='our_customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='service/img/default/default.png', upload_to='service/img/')),
                ('title', models.CharField(max_length=191)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='our_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='service/img/default/default.png', upload_to='service/img/')),
                ('title', models.CharField(max_length=191)),
                ('description', models.TextField()),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('telegram', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='work_samples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='work_samples/img/default/default.png', upload_to='work_samples/img/')),
                ('title', models.CharField(max_length=191)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='service',
            old_name='video_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='video_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='service',
            name='cover_img',
        ),
        migrations.RemoveField(
            model_name='service',
            name='video_url',
        ),
        migrations.AddField(
            model_name='service',
            name='img',
            field=models.ImageField(blank=True, default='service/img/default/default.png', upload_to='service/img/'),
        ),
    ]
