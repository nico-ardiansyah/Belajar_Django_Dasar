# Generated by Django 5.1.2 on 2024-11-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_createpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='banner',
            field=models.FileField(upload_to=''),
        ),
    ]
