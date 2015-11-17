import csv

training_split = csv.writer(open("training_split.csv", "wb"))

# Read in training file
with(open("training.csv","rb")) as f:
    csvreader = csv.reader(f,delimiter =",")
    for index, row in enumerate(csvreader):
        if index%2 == 0:
            training_split.writerow(row)
        
