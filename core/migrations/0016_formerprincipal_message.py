# Generated by Django 3.2 on 2022-09-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_formerprincipal'),
    ]

    operations = [
        migrations.AddField(
            model_name='formerprincipal',
            name='message',
            field=models.TextField(default='default message for previous '),
            preserve_default=False,
        ),
    ]
