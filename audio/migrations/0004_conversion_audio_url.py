# Generated by Django 4.0.4 on 2022-06-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_conversion_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversion',
            name='audio_url',
            field=models.CharField(blank=True, max_length=255, verbose_name='URL to created audio'),
        ),
    ]
