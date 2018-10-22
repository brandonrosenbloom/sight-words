# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from words.models import Words, Grade

# Create your views here.


def home(request):
    grades = Grade.objects.all()

    context = {
        'grades': grades,
    }

    return render(request, 'home.html', context)


def words_by_grade(request, grade):
    if not Words.objects.filter(grade=grade):

        return render(request, 'no_words.html')

    else:
        words = Words.objects.filter(grade=grade)

        context = {
            'words': words,
        }

        return render(request, 'words.html', context)