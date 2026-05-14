from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Subject, StudyQuiz, StudyQuestion, Choice, StudentRecord
@login_required
def run_quiz(request, quiz_id):
    quiz = get_object_or_404(StudyQuiz, pk=quiz_id)
    questions = StudyQuestion.objects.filter(quiz=quiz)
    
    if request.method == 'POST':
        score = 0
        for q in questions:
            # 1. Get the ID from the radio button
            selected_choice_id = request.POST.get(f'q_{q.id}')
            
            # 2. Check if the user actually selected something
            if selected_choice_id:
                try:
                    # 3. Convert ID to integer and find the Choice
                    choice = Choice.objects.get(id=int(selected_choice_id))
                    if choice.is_right:
                        score += 1
                except (ValueError, Choice.DoesNotExist):
                    # If the ID isn't a number or doesn't exist, skip it
                    continue
        
        # Save the result
        StudentRecord.objects.create(
            user=request.user, 
            quiz=quiz, 
            points=score, 
            total_points=questions.count()
        )
        return render(request, 'study_hub/results.html', {'score': score, 'total': questions.count()})

    return render(request, 'study_hub/quiz_page.html', {'quiz': quiz, 'questions': questions})
def dashboard(request):
    subjects = Subject.objects.all()
    return render(request, 'study_hub/dashboard.html', {'subjects': subjects})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})