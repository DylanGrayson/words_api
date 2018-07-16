# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from models import Word
from serializers import WordSerializer


class WordsViewSet(viewsets.ViewSet):

    def add(self, request, format="JSON"):
        if isinstance(request.data, (list,)):
            atLeastOne = False
            for w in request.data:
                data = {'word': w}
                word = WordSerializer(data=data)
                if word.is_valid():
                    atLeastOne = True
                    word.save()
            if atLeastOne:
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def count(self, request, format="JSON"):
        return Response(Word.objects.count(), status=status.HTTP_200_OK)

    def palindrome_count(self, request, format="JSON"):
        return Response(len(Word.objects.filter(isPalindrome=True)), status=status.HTTP_200_OK)

    def anagram_count(self, request, format="JSON"):
        return Response(len(Word.objects.filter(hasAnagram=True)), status=status.HTTP_200_OK)
