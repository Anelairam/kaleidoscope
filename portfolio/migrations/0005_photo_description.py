# Generated by Django 4.1 on 2022-08-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_photo_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]