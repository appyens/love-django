# Generated by Django 3.0.4 on 2020-05-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=17, verbose_name='ISBN-13'),
        ),
    ]
