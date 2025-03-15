from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Journal
from journal_pages.models import Journal_Entry
from django.contrib.auth.decorators import login_required
from . import forms
import logging

logger = logging.getLogger(__name__)


@login_required(login_url="/users/login/")
def journal_list(request):
    # journals = Journal.objects.all().order_by('-start_date')
    journals = Journal.objects.filter(author = request.user.id)
  
    
    return render(request, 'journal_list.html', {'journals': journals} )


@login_required(login_url="/users/login/")
def journal_new(request):
    if request.method == "POST":
        form = forms.JournalForm(request.POST, request.FILES)
        if form.is_valid():
            new_journal = form.save(commit=False)
            new_journal.author = request.user
            new_journal.save()
            return redirect('journal:journal_list')
            
        else:
            return render(request, 'journal_list.html')
    else:
        form = forms.JournalForm()

   
    return render(request, 'journal_form.html', {'form': form})

@login_required(login_url="/users/login/")
def journal_book_view(request, journal_slug):
    # we grab the specific item we need based on the slug value thats auto generated
    journal = Journal.objects.get(slug = journal_slug)
    
    # This ended up being what I needed to do.  
    # I needed to filter the entries based on journal_book corresponding to the journal
    # it works with journal but I prefer to specify journal.id for my own learning
    journal_entry = Journal_Entry.objects.filter(journal_book=journal.id).order_by('-entry_date')
    return render(request, 'journal_book.html', {'journal': journal , 'journal_entry': journal_entry })

def edit_journal_book_view(request, journal_slug):
    journal = get_object_or_404(Journal, slug=journal_slug )
    if request.method =='POST':
        form = forms.JournalForm(request.POST, request.FILES, instance = journal)
        if form.is_valid():
            form.save()

            editted_journal = get_object_or_404(Journal, id = journal.id)
            return redirect('journal:journal_book', editted_journal.slug)
        
        else:
            print("Form Errors", form.errors)

    else:
        form = forms.JournalForm(instance = journal)

    return render (request, 'journal_form.html', {'journal':journal, 'form':form})


def delete_journal_book_view(request, journal_slug):
    journal = get_object_or_404(Journal, slug=journal_slug )
    if request.method == 'POST':
        journal.delete()
        return redirect('/')
    
    return redirect('/')


