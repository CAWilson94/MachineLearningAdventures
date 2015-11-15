import csv
import pandas
from docutils.utils import column_indices
from bsddb.dbtables import contains_metastrings
file = open("Advertising.csv")

#write new file
c = csv.writer(open("boop.csv", "wb"))
#read in original file
readCSV = csv.reader(file,delimiter= ",")

print file.index_col(2)


"""for row in readCSV :
    print "something"
    #if contains(2016)
    if readCSV.index_col(2).Contains('2015') :
        print "2015 spotted"
        c.writerow(row)
        
file.close()"""
    
    
    


