# Generated by Django 5.1 on 2024-09-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=12, null=True),
        ),
    ]