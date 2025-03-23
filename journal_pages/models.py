from django.db import models
from django.utils.text import slugify
from journal.models import Journal
from django.contrib.auth.models import User


# Create your models here.
class Journal_Entry(models.Model):
    entry_title = models.CharField(max_length=50, help_text="What is the title of today's Journal Entry?")
    entry_date =  models.DateField(auto_now_add=True)
    week_entry = models.TextField(max_length=10000, help_text="How did your week go? \nWhat successes did you experience?\
        What did you not achieve this week that you said you will?\n Any magic moments?")
    learn_entry = models.TextField(max_length=10000, help_text="What did I learn \
             in this week?  About myself?  Others? What do I plan to do \
                tomorrow, differently or the same?")
    interact_entry = models.TextField(max_length=10000, help_text="Who did you \
        interact with?  Anyone you need to update?  Who did you thank? Ask a \
        question with? Share info or feedback with?")
    goals_entry = models.TextField(max_length=10000, help_text="What are some \
        goals you have for this next week?")
    journal_book = models.ForeignKey(Journal, on_delete=models.CASCADE, default=None, related_name="journal_book")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    slug = models.SlugField(blank=True, unique=True)

# Just going to slugify the journal entry title... and also going to adjust max field lengths.  Turns out I need more than 1k.
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.entry_title)
        self.slug = base_slug
        super().save(*args, **kwargs)
        



    def __str__(self):
        return self.entry_title