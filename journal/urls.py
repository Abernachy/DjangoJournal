from django.urls import path, include
from . import views

app_name= "journal"

urlpatterns = [
    path('',views.journal_list, name='journal_list' ),
    path('new/', views.journal_new, name='journal_new'),
    path('<slug:journal_slug>/', views.journal_book_view, name="journal_book"),
    path('<slug:journal_slug>/edit', views.edit_journal_book_view, name="edit_journal_book"),
    path('<slug:journal_slug>/delete', views.delete_journal_book_view, name="delete_journal_book"),
    # include works when you want to have it look at the URLs from another url file
    # in this case I want a url => journal-x-x-blah/entries/journal-page-blah
    path('<slug:journal_slug>/entries/', include("journal_pages.urls", namespace="journal_pages"))
]