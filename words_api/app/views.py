# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from models import Word
from serializers import WordSerializer


class WordsViewSet(viewsets.ViewSet):

####### ADDITION ###############################################

    def add(self, request, format="JSON"):
        # Accepts a list of strings, and creates them in the database if they
        # do not exist already.
        if isinstance(request.data, (list,)):
            atLeastOne = False
            for w in request.data:
                data = {'word': w.lower()}
                word = WordSerializer(data=data)
                if word.is_valid():
                    atLeastOne = True
                    word.save()
            if atLeastOne:
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

####### RETRIEVAL ###############################################

    def get_word(self, request, word, format="JSON"):
        # Returns the word or 404 if not found
        try:
            w = Word.objects.get(word=word)
            json = JSONRenderer().render(w.word)
            return Response(json, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_anagrams(self, request, word, format="JSON"):
        # Returns a (potentially empty) list of anagrams
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

####### DELETION #################################################

    def delete(self, request, word, format="JSON"):
        # Deletes the word if found
        try:
            w = Word.objects.get(word=word)
            # if this is one of an anagram pair, update the other angram because
            # it no longer is one.
            anas = Word.objects.exclude(word=word).filter(letters=w.letters)
            if len(anas) == 1:
                anas[0].hasAnagram = False
                anas[0].save()
            w.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete_all(self, request, format="JSON"):
        Word.objects.all().delete()
        return Response(status=status.HTTP_202_ACCEPTED)

####### COUNTING ##################################################

    def count(self, request, format="JSON"):
        json = JSONRenderer().render(Word.objects.count())
        return Response(json, status=status.HTTP_200_OK)

    def palindrome_count(self, request, format="JSON"):
        json = JSONRenderer().render(len(Word.objects.filter(isPalindrome=True)))
        return Response(json, status=status.HTTP_200_OK)

    def anagram_count(self, request, format="JSON"):
        json = JSONRenderer().render(len(Word.objects.filter(hasAnagram=True)))
        return Response(json, status=status.HTTP_200_OK)
