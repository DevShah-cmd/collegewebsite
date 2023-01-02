# Generated by Django 3.2 on 2022-12-05 18:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('image', models.ImageField(upload_to='')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
