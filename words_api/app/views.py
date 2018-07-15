# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from models import Word
from serializers import WordSerializer


class WordsViewSet(viewsets.ViewSet):

    def add(self, request, format="JSON"):
        words = WordSerializer(data=request.data, many=True)
        if words.is_valid():
            words.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def count(self, request, format="JSON"):
        return Response(Word.objects.count(), status=status.HTTP_200_OK)
