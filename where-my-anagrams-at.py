def anagrams(word, words):
    result = []
    for anagram in words:
        if sorted(anagram) == sorted(word):
            result.append(anagram)
    return result
