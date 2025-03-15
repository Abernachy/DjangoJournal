from django.urls import path
from . import views

app_name ="journal_pages"

urlpatterns = [
    path('<slug:journal_entry_slug>', views.journal_entry_view, name="view_journal_entries" ),
    path('new/', views.new_journal_entry_view, name="new_journal_entry" ),
    path('<slug:journal_entry_slug>/delete/', views.delete_journal_entry_view, name="delete_journal_entry"),
    path('<slug:journal_entry_slug>/edit/', views.edit_journal_entry_view, name="edit_journal_entries" )

]