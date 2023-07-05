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

#Open the csv file and read the csv
with open(csvpath) as pybank_file:
    budget = csv.reader(pybank_file)
    
    header=next(budget)
    header_first=next(budget)
    profits_losses_total = profits_losses_total + (int(header_first[1]))
    rowcount = rowcount + 1
    months_list.append(header_first[0])
    previous_value = (int(header_first[1]))

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

print("Total Months:", rowcount)
print("Total: $",profits_losses_total)
#print(monthly_change)
print("Average Change: $",round((sum(monthly_change_list))/(len(monthly_change_list)),2))

max_inc = (max(monthly_change_list))
min_dec = (min(monthly_change_list))

max_inc_index = monthly_change_list.index(max_inc)
min_dec_index = monthly_change_list.index(min_dec)

max_month = months_list[max_inc_index + 1]
min_month = months_list[min_dec_index + 1]

print("Greatest Increase in Profits: " + max_month + " (" + "$" + str(max_inc) +")")
print("Greatest Decrease in Porfites: " + min_month + " (" +"$" + str(min_dec) +")")