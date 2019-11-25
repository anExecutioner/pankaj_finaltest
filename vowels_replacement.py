def removeVowels(word):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        word = word.replace(vowel, 'X')
    return word
    
print(removeVowels("consultadd"))