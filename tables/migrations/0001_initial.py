# Generated by Django 4.2.7 on 2024-03-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_id', models.IntegerField(blank=True, null=True)),
                ('league_name', models.CharField(blank=True, max_length=100, null=True)),
                ('league_country', models.TextField(blank=True, max_length=100, null=True)),
                ('league_logo', models.URLField(blank=True, null=True)),
                ('league_flag', models.URLField(blank=True, null=True)),
                ('league_season', models.IntegerField(blank=True, null=True)),
                ('standings_data', models.JSONField()),
            ],
        ),
    ]
