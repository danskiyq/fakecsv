# Generated by Django 4.0.1 on 2022-01-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakecsv', '0004_alter_schema_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]