# Generated by Django 4.0.2 on 2022-02-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
