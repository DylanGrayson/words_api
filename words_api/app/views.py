# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.core.exceptions import ObjectDoesNotExist
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
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, word, format="JSON"):
        try:
            w = Word.objects.get(word=word)
            w.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete_all(self, request, format="JSON"):
        Word.objects.all().delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    def count(self, request, format="JSON"):
        json = JSONRenderer().render(Word.objects.count())
        return Response(json, status=status.HTTP_200_OK)

    def palindrome_count(self, request, format="JSON"):
        json = JSONRenderer().render(len(Word.objects.filter(isPalindrome=True)))
        return Response(json, status=status.HTTP_200_OK)

    def get_anagrams(self, request, word, format="JSON"):
        charList = list(word)
        charList.sort()
        letters = ''.join(charList)
        anagrams = Word.objects.filter(letters=letters)
        anas = WordSerializer(anagrams, many=True)
        retList = []
        for ana in anas.data:
            retList.append(ana['word'])
        json = JSONRenderer().render(retList)
        return Response(json, status=status.HTTP_200_OK)

    def anagram_count(self, request, format="JSON"):
        json = JSONRenderer().render(len(Word.objects.filter(hasAnagram=True)))
        return Response(json, status=status.HTTP_200_OK)
