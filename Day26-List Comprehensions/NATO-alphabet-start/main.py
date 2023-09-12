#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df=pd.read_csv('.\\NATO-alphabet-start\\nato_phonetic_alphabet.csv')
new_list = {row.letter:row.code for (index,row) in df.iterrows()}


word=input("Enter word: ")
letter=[n.upper() for n in word]


name_list=[new_list[letters] for letters in letter]
print(name_list)

