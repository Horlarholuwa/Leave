# Generated by Django 5.0.6 on 2024-07-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_status_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=5, unique=True, verbose_name='Employee_id')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last_Name')),
                ('first_name', models.CharField(max_length=255, verbose_name='Last_Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email')),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='email',
        ),
    ]