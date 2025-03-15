# Generated by Django 5.1.6 on 2025-02-23 14:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_remove_journal_banner_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='banner_image',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='journal',
            name='journal_type',
            field=models.CharField(default='pancakes', help_text='What type of journal (weekly, learning, scientific, etc) is this?', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journal',
            name='purpose',
            field=models.CharField(default='moar pancakes', help_text='Describe the purpose of this journal', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journal',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journal',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
