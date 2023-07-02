# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze 
# the financial records of your company. You will be given a financial dataset 
# called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

## Your task is to create a Python script that analyzes the records to calculate each of the following values:
#Modules
import os
import csv 

print("Financial Analysis")
print("-----------------------------------------")

#Set path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#Set initial value of the row counter to zero
rowcount = 0
profits_losses_total = 0
monthly_change= 0
#Set initial value of the profit/loss counter to zero

#Open the csv file and read the csv
with open(csvpath) as file:
    budget = csv.reader(file)
    
    header=next(file)
    #print(header)

## The total number of months included in the dataset
## The net total amount of "Profit/Losses" over the entire period
## ****THIS IS YIELDING INCORRECT VALUES**** The changes in "Profit/Losses" over the entire period, and then the average of those changes
## The greatest increase in profits (date and amount) over the entire period
## The greatest decrease in profits (date and amount) over the entire period
## Your analysis should align with the following results: See pic on Boot Camp Spot
## In addition, your final script should both print the analysis to the terminal and export a text file with the results.

    for row in budget:
        rowcount = rowcount + 1
        if (int(row[1])) > 0 or (int(row[1])) < 0:
            profits_losses_total = profits_losses_total + (int(row[1]))

        if (int(row[1])) < 0 or (int(row[1])) > 0:
            monthly_change = (int(row[1])) - monthly_change 
            
    print("Total Months:", rowcount)
    print("Total: $",profits_losses_total)
    #print(monthly_change)
    print("Average Change:$ ",round(monthly_change/rowcount))
    #print("Greatest Increase in profits: $" , index[0], max(index[1]))
    #print("Greatest Decrease in profits: $" , index[0], min(index[1]))