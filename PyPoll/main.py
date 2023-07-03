#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:

##The total number of votes cast

##A complete list of candidates who received votes

##The percentage of votes each candidate won

##The total number of votes each candidate won

##The winner of the election based on popular vote

import os
import csv

#Set path for the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#set up variables here
count = 0
candidate_list = []


#Open the csv file and read the csv
with open(csvpath) as pyroll_file:
    election_csv = csv.reader(pyroll_file)

    #header = next(pyroll_file)

    for row in election_csv:
        count += 1

        if row[2] == (next(iter((row[2])))):
            candidate_list.append(row[2]) != candidate_list
        else: 
            #row[2] != (next(iter((row[2])))):
            candidate_list.append(row[2]) == candidate_list
    

print("Election Results")
print("-----------------------------------------")
print("Total Votes: ", count)
#print(candidate_list)
#print("Winner: ", )


