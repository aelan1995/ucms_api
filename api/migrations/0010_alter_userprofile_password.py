# Generated by Django 4.2.7 on 2023-11-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_userprofile_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
