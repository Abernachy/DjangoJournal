from django import forms
from .import models

class CreateJournalEntry(forms.ModelForm):
    class Meta:
        model = models.Journal_Entry
        fields = ['entry_title', 'week_entry', 'learn_entry' ,\
                  'interact_entry', 'goals_entry', 'journal_book']
        exclude = ['slug', 'journal_book']


class EditJournalEntry(forms.ModelForm):
    class Meta:
        model = models.Journal_Entry
        fields = ['entry_title', 'week_entry', 'learn_entry' ,\
                  'interact_entry', 'goals_entry', 'journal_book']
        exclude = ['slug', 'journal_book']



class JournalEntryForm(forms.ModelForm):
      class Meta:
        model = models.Journal_Entry
        fields = ['entry_title', 'week_entry', 'learn_entry' ,\
                  'interact_entry', 'goals_entry']
        exclude = ['slug', 'journal_book']
        widgets = {
            'entry_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter the title of today's journal entry"}),
            'week_entry': forms.Textarea(attrs={'class': 'form-control', 'rows':10, 'placeholder': "Enter your week entry"}),
            'learn_entry': forms.Textarea(attrs={'class': 'form-control', 'rows':10, 'placeholder': "Enter your learn entry"}),
            'interact_entry': forms.Textarea(attrs={'class': 'form-control', 'rows':10, 'placeholder': "Enter your interaction entry"}),
            'goals_entry': forms.Textarea(attrs={'class': 'form-control', 'rows':10, 'placeholder': "Enter your goals entry"}),
            
        }
