# Generated by Django 4.1.5 on 2023-01-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]