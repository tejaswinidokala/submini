from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Note
import json
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
@csrf_exempt 

# Create your views here.
def index(request):
   return render(request, 'index.html')

def saved_notes(request):
    saved_notes = Note.objects.filter(user=request.user)
    return render(request, 'saved-notes.html', {'saved_notes': saved_notes})
 
 # <-- this is the missing piece!
def save_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')

        if title and content:
            Note.objects.create(
                user=request.user,
                title=title,
                content=content
            )

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing title or content'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

def get_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    data = [{'id': note.id, 'title': note.title, 'content': note.content} for note in notes]
    return JsonResponse(data, safe=False)
@login_required
def delete_note(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})
@csrf_exempt
@login_required
def edit_note(request, note_id):
    if request.method == 'POST':
        
        note = get_object_or_404(Note, id=note_id, user=request.user)
        data = json.loads(request.body)

        note.title = data.get('title')
        note.content = data.get('content')
        note.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=405)