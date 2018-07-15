# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Word(models.Model):
    word = models.CharField(primary_key=True, max_length=100)
    letters = models.CharField(max_length=100)
    length = models.IntegerField()
    isPalindrome = models.BooleanField()
    anagramCount = models.IntegerField(default=0)
