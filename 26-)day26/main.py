import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = pandas.DataFrame(data)
phonetic_dict = {row.letter: row.code for (index, row) in new_data.iterrows()}
word = input("Enter a Word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)