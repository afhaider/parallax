# Generated by Django 2.1.4 on 2019-02-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190228_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml',
            name='zz',
            field=models.ImageField(height_field='400', max_length='800', upload_to='ml', width_field='400'),
        ),
    ]
