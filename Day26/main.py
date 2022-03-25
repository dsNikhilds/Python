# NATO Alphabet Project

import sys
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato = { letter:code   for (letter,code) in zip(df.letter,df.code)}

user = input("Enter a word \n").upper()

alphabet = [nato[letter]  for letter in user]
print(alphabet)

input("     ")
sys.exit()