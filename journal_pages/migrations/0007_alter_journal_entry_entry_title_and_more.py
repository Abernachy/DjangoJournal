# Generated by Django 5.1.6 on 2025-03-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_pages', '0006_alter_journal_entry_goals_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal_entry',
            name='entry_title',
            field=models.CharField(help_text="What is the title of today's Journal Entry?", max_length=50),
        ),
        migrations.AlterField(
            model_name='journal_entry',
            name='goals_entry',
            field=models.TextField(help_text='What are some         goals you have for this next week?', max_length=10000),
        ),
        migrations.AlterField(
            model_name='journal_entry',
            name='interact_entry',
            field=models.TextField(help_text='Who did you         interact with?  Anyone you need to update?  Who did you thank? Ask a         question with? Share info or feedback with?', max_length=10000),
        ),
        migrations.AlterField(
            model_name='journal_entry',
            name='learn_entry',
            field=models.TextField(help_text='What did I learn              in this week?  About myself?  Others? What do I plan to do                 tomorrow, differently or the same?', max_length=10000),
        ),
        migrations.AlterField(
            model_name='journal_entry',
            name='week_entry',
            field=models.TextField(help_text='How did your week go? \nWhat successes did you experience?        What did you not achieve this week that you said you will?\n Any magic moments?', max_length=10000),
        ),
    ]
