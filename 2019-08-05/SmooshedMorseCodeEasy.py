from itertools import product
morseAlphabet = str(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..").split(" ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
keywords = ["sos", "daily", "programmer", "bits", "three"]

morseAlphabet = dict(zip(alphabet, morseAlphabet))

def smorse(word):
    return ''.join([morseAlphabet[letter] for letter in word])

for word in keywords:
    print(word, smorse(word))

with open("2019-08-05/enable1.txt", "r") as f:
    enable = dict([(word, smorse(word)) for word in f.read().splitlines()])
    
#bonus1
#The sequence -...-....-.--. is the code for four
#different words (needing, nervate, niding, tiling).
#Find the only sequence that's the code for 13
#different words.

seqNum = 13
sequences = list(enable.values())
for sequence in sequences:
    if sequences.count(sequence) == seqNum:
        print(sequence)
        break

#bonus2
#autotomous encodes to .-..--------------..-...,
#which has 14 dashes in a row. Find the only word
#that has 15 dashes in a row.

for key,val in enable.items():
    dashCountList = []
    dashCount = 0
    for letter in val:
        if letter == '-':
            dashCount += 1
        else:
            dashCountList.append(dashCount)
            dashCount = 0
    if 15 in dashCountList:
        print(key, val)
        break


#bonus3

#Call a word perfectly balanced if its code has
#the same number of dots as dashes.
#counterdemonstrations is one of two 21-letter
#words that's perfectly balanced.
#Find the other one.
for key, val in enable.items():
    if len(key) == 21:
        dots = val.count('.')
        dashes = val.count('-')
        if dots == dashes and key != "counterdemonstrations":
            print(key, val)
            break

#bonus4

#protectorate is 12 letters long and encodes to
#.--..-.----.-.-.----.-..--., which is a
# palindrome (i.e. the string is the same when
# reversed). Find the only 13-letter word that
# encodes to a palindrome.

for key, val in enable.items():
    if len(key) == 13:    
        if val == val[::-1]:
            print(key, val)
            break
