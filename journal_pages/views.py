from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from journal.models import Journal
from .models import Journal_Entry
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/users/login/")
def new_journal_entry_view(request, journal_slug):
    # get_object_or_404 makes an attempt to get the object and returns 404 if no luck
    # slub object needs to be passed because the url requires it
    journal = get_object_or_404(Journal, slug=journal_slug)
    if request.method == "POST":
        form = forms.JournalEntryForm(request.POST)
        if form.is_valid():
            # code is somewhat copied from the journal_new , debating on just having it save and commit here instead of leaving space for an author field
            new_journal_entry = form.save(commit=False)
            new_journal_entry.author = request.user
            new_journal_entry.journal_book = journal
            new_journal_entry.save()
            # I had to use journal.slug instead of the context object
            return redirect('journal:journal_book',journal.slug)
        else:
            return render(request, 'journal:journal_book')
    else:
        form = forms.JournalEntryForm()

    return render(request, 'journal_entry_form.html', {"journal": journal, 'form': form})
    # return HttpResponse(f"Recieved journal_slug: {journal}")


@login_required(login_url="/users/login/")
def journal_entry_view(request, journal_slug, journal_entry_slug):
    # I need the slug for both the journal and the entry objects
    # I know there is better way because I feel this way would do a query everytime it runs
    # template uses entry.[blah blah]
    journal = get_object_or_404(Journal, slug=journal_slug)
    entry = get_object_or_404(Journal_Entry, slug=journal_entry_slug)
    return render(request, 'journal_page.html' , {"journal": journal, "entry": entry } )


def delete_journal_entry_view(request, journal_slug, journal_entry_slug):
    # Yea, this is a repeat of the above
    journal = get_object_or_404(Journal, slug=journal_slug)
    entry = get_object_or_404(Journal_Entry, slug=journal_entry_slug)

    if request.method =="POST":
        entry.delete()
        messages.success(request, "Journal Entry Successfully Deleted")
        return redirect('journal:journal_book', journal.slug)
    
    return redirect('journal:journal_book', journal.slug)

def edit_journal_entry_view(request, journal_slug, journal_entry_slug):
    journal = get_object_or_404(Journal, slug=journal_slug)
    entry = get_object_or_404(Journal_Entry, slug=journal_entry_slug)

    if request.method =='POST':
        form = forms.JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            print("Form is valid")
            form.save()
            
            # I want to go back to viewing the journal but I need the new slug
            editted_entry = get_object_or_404(Journal_Entry, id = entry.id)
            return redirect('journal:journal_pages:view_journal_entries', journal.slug ,editted_entry.slug)
        else:
            print("Form errors", form.errors)
    else:
        form = forms.JournalEntryForm(instance=entry)
        

    return render(request, 'journal_entry_form.html', {"journal": journal, "entry":entry, 'form':form})

