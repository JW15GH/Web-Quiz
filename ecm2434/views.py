from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Question
from leaderboard.models import Score
from .models import Quiz, Question
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

def about(request):
    return render(request, 'ecm2434/about.html')

def priv_pol(request):
    return render(request, 'ecm2434/privacypolicy.html')

@login_required
def article_one(request):
    # Check if user has already been awarded points for visiting the page
    if request.session.get('visited_article_one', False):
        print("User already visited, no points awarded")  # Debug print
        return render(request, 'ecm2434/articleone.html')
    else:
        # Award points to the user
        user_score = Score.objects.get(player=request.user)  # Modify this line
        points_awarded = 10  # Set the number of points to be awarded
        user_score.score += points_awarded
        user_score.save()
        print(f"Awarded points: {points_awarded}, New score: {user_score.score}")  # Debug print

        # Mark the user as having visited the page
        request.session['visited_article_one'] = True
        print(f"User visited for the first time, awarded {points_awarded} points")  # Debug print
        return render(request, 'ecm2434/articleone.html')

@login_required
def profile(request):
    # Retrieve the quiz you want to display
    quiz = Quiz.objects.get(name='q1')
    # Retrieve all the questions for the quiz
    questions = Question.objects.filter(quiz=quiz)
    # Render the quiz template with the quiz and questions context variables
    return render(request, 'ecm2434/q1.html', {'quiz': quiz, 'questions': questions})

def answer(request):
    if request.method == 'POST':
        user_score = 0
        quiz = Quiz.objects.get(name='q1')
        questions = Question.objects.filter(quiz=quiz)

        # Count the number of correct answers and award points accordingly
        num_correct = 0
        for question in questions:
            # Get the submitted answer for the current question
            submitted_answer = request.POST.get(f'answer_{question.id}')

            # If the submitted answer is correct, increment the count of correct answers
            if submitted_answer == question.correct_answer:
                num_correct += 1

        if request.session.get('visited_quiz_one', False):
            score = Score.objects.filter(player=request.user).first()
            return render(request, 'ecm2434/score.html', {'score': score.score, 'num_correct': num_correct})
        else:
            if num_correct == 1:
                user_score += 10
            elif num_correct == 2:
                user_score += 20
            elif num_correct == 3:
                user_score += 30

            # Save the user's score
            user = request.user
            score, created = Score.objects.get_or_create(player=user)
            score.score += user_score
            score.save()

            # Mark the user as having visited the quiz page
            request.session['visited_quiz_one'] = True

        # Return a template with the updated score and number of correct answers included as context variables
        return render(request, 'ecm2434/score.html', {'score': score.score, 'num_correct': num_correct})

    else:
        # Handle the case where the user navigates to this URL directly
        # without submitting a form (e.g., redirect to the profile page)
        return redirect('profile')


def scan_qr(request):
    if request.method == 'POST':
        # Read the image from the POST request
        image = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)

        # Decode the QR code
        decoded_objects = pyzbar.decode(image)

        # Extract the data from the QR code
        if len(decoded_objects) > 0:
            data = decoded_objects[0].data.decode('utf-8')
            # Redirect to the specified URL with the QR code data as a query parameter
            return redirect(data)
        else:
            data = 'No QR code detected'

    # Render the initial form
    return render(request, 'qr_code_scanner.html')
