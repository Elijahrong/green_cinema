# Generated by Django 4.0.2 on 2022-02-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('0.5', 0.5), ('1', 1), ('1.5', 1.5), ('2', 2), ('2.5', 2.5), ('3', 3), ('3.5', 3.5), ('4', 4), ('4.5', 4.5), ('5', 5)], default='5', max_length=3),
        ),
    ]
