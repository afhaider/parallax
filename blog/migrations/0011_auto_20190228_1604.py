# Generated by Django 2.1.4 on 2019-02-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190228_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml',
            name='zz',
            field=models.FileField(upload_to=''),
        ),
    ]
