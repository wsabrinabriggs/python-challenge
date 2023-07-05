import os
import csv

#Set path for the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#set up variables here (optional)
count = 0
candidate_list = []
all_candidates_list = []
sorted_all_candidates_list = []
candidate = []
ccs_votes = []
dd_votes = []
rad_votes = []

#Open the csv file and read the csv
with open(csvpath) as pyroll_file:
    election_csv = csv.reader(pyroll_file)
    
    header = next(election_csv)
    # print(header) 
    # print(header[0])


    for row in election_csv:
        count += 1
#includes all of the votes for each candidate        
        all_candidates_list.append(row[2])
#sorts the candidates votes into their own list
        if row[2] == "Charles Casper Stockham":
            ccs_votes.append(row[2])
        if row[2] == "Diana DeGette":
            dd_votes.append(row[2])
        if row[2] == "Raymon Anthony Doane":
            rad_votes.append(row[2])

#the candidates names listed only once        
        if row[2] not in candidate_list:
            candidate_list.append(row[2]) 

# ccs_votes = len(all_candidates_list[0])
# dd_votes = len(all_candidates_list[19723:])
# rad_votes = len(all_candidates_list[37686:])

# print(ccs_votes)
# print(dd_votes)
# print(rad_votes)



    # print(len(candidate_list[0]))    
    # print(len(candidate_list[1]))
    # print(len(candidate_list[2]))    

#tells how many votes each candidate got
# print(len(ccs_votes))
# print(len(dd_votes))
# print(len(rad_votes))

# print(len(sorted_all_candidates_list))
#shows the index of each candidate from the sorted_all_candidates_list
#print(sorted_all_candidates_list.index("Charles Casper Stockham"))
# print(sorted_all_candidates_list.index("Diana DeGette"))
# print(sorted_all_candidates_list.index("Raymon Anthony Doane"))

## print(len(all_candidates_list))
#shows the index of each candidate from the all_candidates_list
# print(all_candidates_list.index("Charles Casper Stockham"))
# print(all_candidates_list.index("Diana DeGette"))
# print(all_candidates_list.index("Raymon Anthony Doane"))
#print(len(all_candidates_list))

#percentages of the votes
ccs_votes_deci = (int(len(ccs_votes)))/count
ccs_votes_percent = ("{:.3%}".format(ccs_votes_deci))

dd_votes_deci = (int(len(dd_votes)))/count
dd_votes_percent = ("{:.3%}".format(dd_votes_deci))

rad_votes_deci = (int(len(rad_votes)))/count
rad_votes_percent = ("{:.3%}".format(rad_votes_deci))

#HOW TO CONVERT TO PERCENT from https://www.geeksforgeeks.org/how-to-convert-fraction-to-percent-in-python/ 
# input an negative integer with denominator =1 
# integer_num = -7 
# print ("Converting number to percentage rounding to 5 place of decimal")
# print ("{:.5%}".format(integer_num))


print("Election Results")
print("-----------------------------------------")
print("Total Votes: ", count)
print("-----------------------------------------")
#print(candidate_list)
print(candidate_list[0], ccs_votes_percent, "(",(len(ccs_votes)),")")          
print(candidate_list[1], dd_votes_percent, "(",(len(dd_votes)),")")
print(candidate_list[2], rad_votes_percent, "(",(len(rad_votes)),")")
print("-----------------------------------------")

#to determine winner of election
if len(ccs_votes) > len(dd_votes) and len(rad_votes):
    print("Winner: Charles Casper Stockham")
elif len(dd_votes) > len(ccs_votes) and len(rad_votes):
    print("Winner: Diana DeGette")
elif len(rad_votes) > len(ccs_votes) and len(dd_votes):
    print("Winner: Raymon Anthony Doane")
print("-----------------------------------------")
