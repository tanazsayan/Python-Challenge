 
import csv 
import os
budget_data =  os.path.join("Resources/budget_data.csv")
with open (budget_data) as csvfile:
    reader = csv.reader(csvfile)
    header = next (reader)
    total_profit_loss = 0
    Total_months = 0 
    greatest_increase = 0
    greatest_decrease = 0
    last_month = None
    net_changes = []
    
    row1 = next (reader)
    prev_month = 0
    
    for row in reader:
        total_profit_loss +=int(row[1])
        #print(row)
        
        if last_month is not None and greatest_increase < int(row[1])- last_month:
            greatest_increase = int(row[1]) - last_month
            
        if last_month is not None and greatest_decrease > int(row[1]) - last_month:
            greatest_decrease = int(row[1]) - last_month
        Total_months += 1
        
        last_month = int(row[1])
        
        net_change =  int(row[1]) - prev_month
        prev_month = int(row[1])
        net_changes.append(net_change) 
        
         
    print(Total_months)  
    print(total_profit_loss)
    print(greatest_increase)
    print(greatest_decrease)
    print(net_changes)      
    
    
    
