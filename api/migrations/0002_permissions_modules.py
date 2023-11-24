# Generated by Django 4.2.7 on 2023-11-23 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions_name', models.CharField(max_length=50, unique=True)),
                ('permissions_created', models.DateTimeField(auto_now_add=True)),
                ('permission_status_check', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['permissions_created'],
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modules_created', models.DateTimeField(auto_now_add=True)),
                ('modules_name', models.BooleanField(default=False)),
                ('permissions_checklist', models.ManyToManyField(to='api.permissions')),
                ('roles_dp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roles')),
            ],
            options={
                'ordering': ['modules_created'],
            },
        ),
    ]