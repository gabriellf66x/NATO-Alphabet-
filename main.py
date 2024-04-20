import pandas

# "".csv already a dataframe ""
data = pandas.read_csv("nato_phonetic_alphabet.csv")


# Loop through rows of a data frame

def generate_phonetic():
    text = input("Type any word to convert to NATO: ").upper()
    try:
        phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
        output_list = [phonetic_dict[letter] for letter in text]
    except KeyError:
        print("Enter a valid letter.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
