import pandas

# "".csv already a dataframe ""
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame

text = input("Type any word to convert to NATO: ")
my_list = list(text)

pain = [row.code for i in my_list for (index, row) in data.iterrows() if row.letter == i]

print(pain)















