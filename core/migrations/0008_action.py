# Generated by Django 3.2 on 2022-09-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('action', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=500)),
                ('link_text', models.CharField(max_length=25)),
            ],
        ),
    ]
