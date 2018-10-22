# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Words(models.Model):
    word = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)

    def __str__(self):
        return self.word
