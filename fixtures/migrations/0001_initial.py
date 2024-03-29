# Generated by Django 4.2.7 on 2024-03-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_id', models.IntegerField()),
                ('league_name', models.CharField(max_length=100)),
                ('league_season', models.IntegerField()),
                ('league_round', models.CharField(max_length=100)),
                ('fixture_id', models.IntegerField()),
                ('fixture_timestamp', models.IntegerField()),
            ],
        ),
    ]
