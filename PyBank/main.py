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
budget = []
profits_losses_total = 0
monthly_change = 0
gip = 0
gdp = 0


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
#total number of rows/months
        rowcount = rowcount + 1
        print(file)
#total profits/losses
        #if (int(row[1])) >= 0 or (int(row[1])) <= 0: 
            #profits_losses_total = profits_losses_total + (int(row[1])) 
#changes in profits/losses ****THIS IS YIELDING INCORRECT VALUES**** 
        #current_month = [int(row[1])]
        #next_month = current_month 
        #if current_month > 0 or current_month < 0:
         #   monthly_change = current_month
        #print(current_month) 
        #revenue = 0
        #revenue = [int(current_month[0])]
        #print(revenue)
        #print(int(current_month[0]))

        
        #     budget = current_month 
        #monthly_change = next_month - current_month
        # #print(current_month) 
        
            
            #print((int(row[1])))
            #monthly_change = (int(row[1])) - (int(monthly_change))
            #print(monthly_change)
#the greatest increase in profits (date and amount) ****THIS IS YIELDING INCORRECT VALUES**** 
#         if (int(row[1])) > 0 and (int(row[1])) != 0:  
#             #gip = (int(row[1])) 
#             gip = (max(row))   
# #the greatest decrease in profits (date and amount) ****THIS IS YIELDING INCORRECT VALUES**** 
#         if (int(row[1])) < 0 and (int(row[1])) != 0:  
#             #gdp = (int(row[1])) 
#             gdp = (min(row))
#     print("Total Months:", rowcount)
#     print("Total: $",profits_losses_total)
#     # #print(monthly_change)
#     print("Average Change: $",round(monthly_change/rowcount))
#     print("Greatest Increase in profits: $" , row[0], (max(row))) 
#     print("Greatest Decrease in profits: $" , row[0], (min(row))) 
    