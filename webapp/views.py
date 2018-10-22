# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from words.models import Words, Grade
from django.contrib.auth.models import User
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def grades(request):
    grades = Grade.objects.all()

    context = {
        'grades': grades,
    }

    return render(request, 'grades.html', context)


def words_by_grade(request, grade):
    if not Words.objects.filter(grade=grade):

        return render(request, 'no_words.html')

    else:
        words = Words.objects.filter(grade=grade)
        grade = Grade.objects.filter(id=grade).first

        context = {
            'words': words,
            'grade': grade,
        }

        return render(request, 'words.html', context)


def feedback(request):
    if not Feedback.objects.filter(active=True):
        return render(request, 'no_feedback.html')

    else:
        all_feedback = Feedback.objects.filter(active=True)

        context = {
            'all_feedback': all_feedback,
        }

        return render(request, 'feedback.html', context)


def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.submitted_by_id = 1
            # post.published_date = timezone.now()
            form.save()

            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'add_feedback.html', {'form': form})
