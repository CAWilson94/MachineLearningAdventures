import csv
# write new file
training = csv.writer(open("training.csv", "wb"))
test = csv.writer(open("test.csv", "wb"))
# read in original file
with open("Advertising.csv", "rb") as f:
    csvreader = csv.reader(f, delimiter=",")
    for row in csvreader :
    # if contains(2016)
        if "37" in row[2]:
            print "2015 spotted"
            training.writerow(row)
    

    
    
    


