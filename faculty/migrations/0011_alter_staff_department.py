# Generated by Django 4.1 on 2022-12-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_alter_department_name'),
        ('faculty', '0010_rename_number_position_staff_number_in_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='departments.department'),
        ),
    ]