import csv

# Write training and testing files
training = csv.writer(open("training.csv", "wb"))
testing = csv.writer(open("testing.csv", "wb"))

# Read in original file
with open("pp-complete.csv", "rb") as f:
    csvreader = csv.reader(f, delimiter=",")
    # Split up data
    for row in csvreader :
        if "2015" in row[2]:
            print "2015 spotted"
            testing.writerow(row)
        else:
            training.writerow(row)
    

    
    
    


