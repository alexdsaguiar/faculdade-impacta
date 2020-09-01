s=("abc ")
vowel=0
consonant=0
for letter in s:
    if letter in "aeiou":
        vowel=vowel+1
    else:
        consonant=consonant+1
print(vowel+consonant)
