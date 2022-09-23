# Generated by Django 4.1 on 2022-09-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('day', models.DateField()),
                ('starting_at', models.TimeField()),
                ('ending_at', models.TimeField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]