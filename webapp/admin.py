# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from words.models import Words, Grade
from feedback.models import Feedback


admin.site.register(Words)

admin.site.register(Grade)

admin.site.register(Feedback)