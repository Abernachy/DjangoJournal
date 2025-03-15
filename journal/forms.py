from django import forms 
from .import models

# Turns out I can just make the form dynamic and I only really need 1 form
# class CreateJournal(forms.ModelForm):
# #     class Meta:
# #         model = models.Journal
# #         fields = ['journal_title', 'purpose', 'journal_type', 'banner_image']
# #         exclude = ['slug']
# #         widgets = {
# #             'journal_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter the title of your journal book"}),
# #             'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows':4, 'placeholder': 'Describe the purpose of this journal'}),
# #             'journal_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What type of journal is this?'}),
# #             'banner_image': forms.FileInput(attrs={'class':'form-control'})
# #         }

# # class EditJournal(forms.ModelForm):
# #     class Meta:
# #         model = models.Journal
# #         fields = ['journal_title', 'purpose', 'journal_type', 'banner_image']
# #         exclude = ['slug']



class JournalForm(forms.ModelForm):
    class Meta:
        model = models.Journal
        fields = ['journal_title', 'purpose', 'journal_type', 'banner_image']
        exclude = ['slug']
        widgets = {
            'journal_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter the title of your journal book"}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'rows':4, 'placeholder': 'Describe the purpose of this journal'}),
            'journal_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What type of journal is this?'}),
            'banner_image': forms.FileInput(attrs={'class':'form-control'})
        }
