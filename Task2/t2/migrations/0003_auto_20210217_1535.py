# Generated by Django 3.1.4 on 2021-02-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t2', '0002_auto_20210217_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_all',
            name='Picture',
            field=models.FileField(blank=True, upload_to='user_Image'),
        ),
    ]
