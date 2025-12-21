from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Note
import json
from django.utils import timezone 
@csrf_exempt 

# Create your views here.
def index(request):
   return render(request, 'index.html')

def saved_notes(request):
    saved_notes = Note.objects.all()
    return render(request, 'saved-notes.html', {'saved_notes': saved_notes})
 
 # <-- this is the missing piece!
def save_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')

        if title and content:
            Note.objects.create(title=title, content=content)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing title or content'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

def get_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    data = [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]
    return JsonResponse(data, safe=False)

def delete_note(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return JsonResponse({'status': 'success'})
        except Note.DoesNotExist:
            return JsonResponse({'status': 'fail'})
@csrf_exempt
def edit_note(request, note_id):
    if request.method == 'POST':
        try:
            note = Note.objects.get(id=note_id)
            data = json.loads(request.body)

            note.title = data.get('title', note.title)
            note.content = data.get('content', note.content)
            note.save()

            return JsonResponse({'status': 'success'})
        except Note.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)

    return JsonResponse({'status': 'error'}, status=405)