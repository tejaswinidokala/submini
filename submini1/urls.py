# submini1/urls.py (app-level)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('index/', views.index, name='index'),
    path('saved-notes/', views.saved_notes, name='saved_notes'),
    path('api/save_note/', views.save_note, name='save_note'),
    path('api/get_notes/', views.get_notes, name='get_notes'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),


]
