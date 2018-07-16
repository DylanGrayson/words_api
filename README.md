# words_api
simple word querying RESTful API


This is a JSON only API.

# Adding words:
POST /words  BODY= '["word1", ...]'
- Returns 201 if at least one word in the list was added
- Returns 204 if none of the words were added (already exist, or too long)
- Returns 400 if input is bad

# Retrieving words:
GET /words/<word>
- Returns 200 and <word> if it exists
- Returns 404 if it doesn't exists

GET /anagrams/<word>
- Returns 200 and a (potentially empty) list of anagrams of <word>

# Deleting words:
DELETE /words
- Returns 202 and deletes all words in the database

DELETE /words/<word>
- Returns 202 and deletes <word> if it exists
- Returns 404 if it doesn't exists

# Counting words:
GET /counts/words
- Returns 200 and the number of words in the database

GET /counts/anagrams
- Returns 200 and the number of words that are anagrams with another word in the database.
Note: This can never return 1, because if there is 1 anagram, there is at least one other.

GET /counts/palindromes
- Returns 200 and the number of palindromes in the database

# Technical details
This solution does most of the computation on addition and deletion of words, as can be seen in the create function of the WordSerializer in serializers.py. This is because I assume details about the words will be queried more often then the words themselves are added or deleted. This way I only check if a word is a palindrome once on addition, then the query to get all palindromes is very fast. Anagrams are handled in a similar way, but need to be considered on deletion as well. If two words were anagrams with each other and no other words, then when I delete one of them, the other is no longer an anagram, and should be updated accordingly.
