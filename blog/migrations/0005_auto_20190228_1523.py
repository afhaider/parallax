# Generated by Django 2.1.4 on 2019-02-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_ml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml',
            name='zz',
            field=models.ImageField(blank=True, upload_to='m_l'),
        ),
    ]
