# Generated by Django 4.0.2 on 2022-02-03 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('genre', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('cast', models.CharField(blank=True, max_length=200, null=True)),
                ('film_rating_system', models.CharField(blank=True, max_length=20, null=True)),
                ('information', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(db_column='movie_id', on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movie.movie')),
            ],
            options={
                'db_table': 'rating',
            },
        ),
    ]
