# Generated by Django 4.0.4 on 2022-06-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_remove_conversion_audio_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversion',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Video title'),
        ),
    ]