# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from words.models import Words, Grade
from django.contrib.auth.models import User
from feedback.models import Feedback

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
