# Generated by Django 3.2 on 2022-12-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_staff_head_of_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]