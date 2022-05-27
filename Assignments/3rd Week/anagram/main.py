# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    if len(word) == len(anagram):
            if (sorted(word) == sorted(anagram)):
                return True
                
    return False

print(find_anagrams("word", "owdr"))
print(find_anagrams("hello", "check") )
print(find_anagrams("below", "elbow") )
