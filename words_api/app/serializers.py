
from rest_framework import serializers
from models import Word
from django.core.exceptions import ObjectDoesNotExist
from utils import isPalindrome

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word',)

    def create(self, validated_data):
        word = validated_data['word']
        try:
            Word.objects.get(word=word)
        except ObjectDoesNotExist:
            charList = list(word)
            charList.sort()
            palindrome = isPalindrome(word)
            letters = ''.join(charList)
            hasAna = False
            anas = Word.objects.filter(letters=letters)
            numAnas = len(anas)
            if numAnas > 0:
                hasAna = True
                if numAnas == 1:
                    anas[0].hasAnagram = True
                    anas[0].save()

            w = Word(word = word,
                letters = letters,
                length = len(word),
                isPalindrome = isPalindrome(word),
                hasAnagram = hasAna)
            w.save()
            return w

    def update(self, instance, validated_data):
        instance.hasAnagram = validated_data.get('hasAnagram', instance.hasAnagram)
        return instance
