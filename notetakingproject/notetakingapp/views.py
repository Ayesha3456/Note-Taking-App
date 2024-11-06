from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.utils import timezone

# Home view to display all notes
def home(request):
    notes = Note.objects.all()
    return render(request, 'notetaking.html', {'notes': notes})

# Create note view
def create_note(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        category = request.POST.get('category', 'Other')  # Default category if not provided
        
        note = Note(
            name=name,
            description=description,
            priority=priority,
            category=category
        )
        note.save()
        return redirect('home')
    
    return redirect('home')

# Update note view
def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.name = request.POST.get('pname')
        note.description = request.POST.get('description')
        note.priority = request.POST.get('priority')
        note.category = request.POST.get('category', 'Other')  # Default category if not provided
        
        note.save()
        return redirect('home')

    return redirect('home')

# Delete note view
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')

    return redirect('home')
