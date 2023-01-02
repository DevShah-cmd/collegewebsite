# Generated by Django 3.2 on 2022-12-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_news_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='header',
            name='content',
        ),
        migrations.RemoveField(
            model_name='header',
            name='heading',
        ),
    ]
