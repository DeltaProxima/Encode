# Generated by Django 3.2.7 on 2022-01-10 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0007_auto_20220110_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busNumber', models.CharField(default='', max_length=100)),
                ('route', models.CharField(default='', max_length=100000)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile')),
            ],
        ),
    ]
