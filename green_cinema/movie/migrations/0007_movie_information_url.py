# Generated by Django 4.0.2 on 2022-02-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_rating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='information_url',
            field=models.URLField(blank=True),
        ),
    ]
