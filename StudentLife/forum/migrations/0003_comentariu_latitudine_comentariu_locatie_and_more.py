# Generated by Django 5.1.5 on 2025-01-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_topic_latitudine_topic_longitudine'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariu',
            name='latitudine',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comentariu',
            name='locatie',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comentariu',
            name='longitudine',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
