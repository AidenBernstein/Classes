#Author Name: Aiden Bernstein
#Date: 10/30/2022
#Program Name: Bernstein_vowel_less.py
#Purpose: remove all vowels from a sentence

def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sentence = input("Please enter a sentence: ")
    for letter in vowels:
        sentence = sentence.replace(letter, '')
    print('Disemvowled sentece: ' + sentence)

main()