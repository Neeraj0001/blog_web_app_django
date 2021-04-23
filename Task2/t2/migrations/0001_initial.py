# Generated by Django 3.1.4 on 2021-02-17 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Phone', models.CharField(max_length=200, null=True)),
                ('Account_No', models.CharField(max_length=200, null=True)),
                ('Debit_Card_No', models.CharField(max_length=200, null=True)),
                ('Exp_Date', models.DateField(blank=True, null=True)),
                ('profile_pics', models.ImageField(blank=True, default='unknown.png', null=True, upload_to='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=5000)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Picture', models.ImageField(blank=True, upload_to='user_Image')),
                ('Mode', models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE')], default='PRIVATE', max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_private',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=5000)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Picture', models.ImageField(blank=True, upload_to='user_Image')),
                ('Mode', models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE')], default='PRIVATE', max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=5000)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Picture', models.ImageField(blank=True, upload_to='user_Image')),
                ('Mode', models.CharField(choices=[('public', 'PUBLIC'), ('private', 'PRIVATE')], default='PUBLIC', max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
