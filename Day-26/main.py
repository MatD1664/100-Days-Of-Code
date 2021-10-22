import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alpha", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
NATO = {row.letter:row.code for (index, row) in df.iterrows()}
print(NATO)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [NATO[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
