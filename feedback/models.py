# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    submitted_by = models.ForeignKey(User, on_delete=models.PROTECT)
