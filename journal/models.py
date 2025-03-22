from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.

class Journal(models.Model):
    journal_title = models.CharField(max_length=300, help_text="What is the title of the journal book?", unique=True)
    purpose = models.CharField(max_length=300, help_text= "Describe the purpose of this journal")
    journal_type = models.CharField(max_length=50, help_text="What type of journal (weekly, learning, scientific, etc) is this?")
    start_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    banner_image=models.ImageField(upload_to="journal_banners/", default='fallback.png', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


# Trying to do self.pk or fucking with the dates for some reason returns them as NoneTypes when its saving/retrieving.  I'll just do the normal slugify of the journal title, though can open a problem if there's multiple journal titles that are the same.

    def save(self, *args, **kwargs):
            base_slug = slugify(self.journal_title)
            self.slug = base_slug
            super().save(*args, **kwargs)


   

    def __str__(self):
        return self.journal_title
    


