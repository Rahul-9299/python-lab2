def unique_vowels(sentence):
    vowels = set('aeiouAEIOU')
    vowels_set = set()
    for ch in sentence:
        if ch in vowels:
            vowels_set.add(ch.lower())
    return vowels_set

s = input("Enter a sentence: ")
vowel_set = unique_vowels(s)
print(f"Unique vowels used: {vowel_set}")