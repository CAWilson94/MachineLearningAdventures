import csv
from docutils.utils.punctuation_chars import delimiters
file = open("pp-complete.csv")
readCSV = csv.reader(file,delimiter= ",")
for row in readCSV:
    print(row)
file.close()