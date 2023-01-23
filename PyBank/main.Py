import os
import csv

budget_csv = os.path.join("Resources/budget_data.csv")

total_months = 0
net_total = 0
value = 0
change_list = []
dates = []


with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    # Reading the header
    csvheader = next(csvreader)
    
    # Reading the first row after the header
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    value = int(first_row[1])
    
    # Using for loop to go thru each columns in datafile
    
    for row in csvreader:
        
        # Calculate total months
        total_months +=1
        
        #Calculate total net
        net_total += int(row[1])
        
        # Appending dates to date list
        dates.append(row[0])
        
        # Calculate the change and append it to list
        change = int(row[1]) - value
        change_list.append(change)
        value = int(row[1])
        
        # Calculate greatest increase
        greatest_incr = max(change_list)
        index_i = change_list.index(greatest_incr)
        date_i = dates[index_i]
       
        # Calculate greatest decrease
        greatest_decr = min(change_list)
        index_d = change_list.index(greatest_decr)
        date_d = dates[index_d]

        # Calculate Average Change
        avg_change = sum(change_list)/len(change_list)
        
# Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {date_i} (${str(greatest_incr)})")
print(f"Greatest Decrease in Profits: {date_d} (${str(greatest_decr)})")

# Printing to analysis.txt
textfile = os.path.join("Analysis", "analysis.txt")
with open(textfile,"w") as textfile:
    print("Financial Analysis", file=textfile)
    print("---------------------", file=textfile)
    print(f"Total Months: {str(total_months)}", file=textfile)
    print(f"Total: ${str(net_total)}", file=textfile)
    print(f"Average Change: ${str(round(avg_change,2))}", file=textfile)
    print(f"Greatest Increase in Profits: {date_i} (${str(greatest_incr)})", file=textfile)
    print(f"Greatest Decrease in Profits: {date_d} (${str(greatest_decr)})", file=textfile)


    
    
