# Generated by Django 5.1 on 2024-09-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_category_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='addbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('author', models.CharField(max_length=12)),
                ('coverphoto', models.FileField(upload_to='media')),
            ],
        ),
    ]