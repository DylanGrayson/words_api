"""words_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^words/?$', views.WordsViewSet.as_view({'post': 'add', 'delete': 'delete_all'})),
    url(r'^words/(?P<word>[a-zA-Z]+)/?$', views.WordsViewSet.as_view({'get': 'get_word', 'delete': 'delete'})),
    url(r'^anagrams/(?P<word>[a-zA-Z]+)/?$', views.WordsViewSet.as_view({'get': 'get_anagrams'})),

    url(r'^counts/words/?$', views.WordsViewSet.as_view({'get': 'count'})),
    url(r'^counts/palindromes/?$', views.WordsViewSet.as_view({'get': 'palindrome_count'})),
    url(r'^counts/anagrams/?$', views.WordsViewSet.as_view({'get': 'anagram_count'}))
]
