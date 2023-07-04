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
months_list = []
budget_list = []
monthly_change = 0
monthly_change_list = []
budget = 0
gip = 0
gdp = 0


#Open the csv file and read the csv
with open(csvpath) as pybank_file:
    budget = csv.reader(pybank_file)
    
    header=next(budget)
    #print(header)
    header_first=next(budget)
    profits_losses_total = profits_losses_total + (int(header_first[1]))
    rowcount = rowcount + 1
    months_list.append(header_first[0])
    previous_value = (int(header_first[1]))
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
        budget_list = [(row[0]), (int(row[1]))]
        months_list.append(row[0])
#total profits/losses
        profits_losses_total = profits_losses_total + (int(row[1]))
        monthly_change = (int(row[1])) - previous_value
        previous_value = (int(row[1]))
        monthly_change_list.append(monthly_change)              
#changes in "Profit/Losses" over the entire period, and then the average of those changes ****THIS IS YIELDING INCORRECT VALUES**** 
# monthly_change = monthly_change - (budget_list[1])
# monthly_change = next_month - current_month
#the greatest increase in profits (date and amount) ****THIS IS YIELDING INCORRECT VALUES**** 
# for row in budget_list:
#     if budget_list[1] > 0:  
#         gip = budget_list[1]
#print(budget_list)   
# #the greatest decrease in profits (date and amount) ****THIS IS YIELDING INCORRECT VALUES**** 
#         if (int(row[1])) < 0 and (int(row[1])) != 0:  
#             #gdp = (int(row[1])) 
#             gdp = (min(row))
print("Total Months:", rowcount)
print("Total: $",profits_losses_total)
#print(monthly_change)
print("Average Change: $",round((sum(monthly_change_list))/(len(monthly_change_list)),2))

max_inc = (max(monthly_change_list))
min_dec = (min(monthly_change_list))

max_inc_index = monthly_change_list.index(max_inc)
min_dec_index = monthly_change_list.index(min_dec)

max_month = months_list[max_inc_index + 1]
#print(months_list)
min_month = months_list[min_dec_index + 1]

print("Greatest Increase in Profits: " + max_month + " (" + "$" + str(max_inc) +")")
print("Greatest Decrease in Porfites: " + min_month + " (" +"$" + str(min_dec) +")")

#     print("Greatest Increase in profits: $" , row[0], (max(row))) 
#     print("Greatest Decrease in profits: $" , row[0], (min(row))) 
    