# Generated by Django 4.0.1 on 2022-01-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakecsv', '0003_schema_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='file',
            field=models.FilePathField(),
        ),
    ]