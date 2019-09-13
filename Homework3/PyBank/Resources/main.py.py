# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:11:31 2019

@author: Aalok Devkota
"""

#Import Dependencies
import csv
import os

print("Financial Analysis")
print('-------------------')

#Open the file to be evaluated. It is in the Resources folder.
budget_data_csv = os.path.join("../Resources", "budget_data.csv")
with open (budget_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #Read the file.
    
    csv_header = next(csvfile) #Skip header
    
# Identify the total-months by counting rows.      
    total_months = sum(1 for row in csvreader)
    print(f'Total number of months: {total_months}' )
  
with open (budget_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    total_sum = 0   #set the sum to 0 as we will be adding to it.
    
    for row in csv.reader(csvfile):
        total_sum += int(row[1]) #Adding integer values to the total sum
       
    print (f'Total Sum: ${total_sum}') # Total Sum is the calculated total of all the values
   
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    date = [] #Create a new list that holds dates (index0)
    profit_loss_list=[] # Create a  list that holds Profit and Loss (index 1)
    monthly_change_list = [] # Create a new list to store the changes from Profit and Loss (index2)
   
    for row in csv.reader(csvfile):
        date.append(row[0]) # Adding dates to date list
        profit_loss_list.append(row[1]) # Adding P&L to the list
        #print (new_list)
    
    n= len(profit_loss_list) #Lenthg of the Profit and Loss list
    i=0     #set the counter to 0
        
    while i < n-1: #Looks for the difference till the value reaches the last one
        monthly_change_list.append(int(profit_loss_list[i+1])-int(profit_loss_list[i]))
        i+=1
    average_change = sum(monthly_change_list)/float(len(monthly_change_list))
    average_change = round(average_change,2)
    print (f'Average Change: ${average_change}')
    max_value = max(monthly_change_list)
    min_value = min(monthly_change_list)
    
    new_max_value_index = monthly_change_list.index(max_value) + 1 #Adding one to match date with change
    #print(new_max_value_index)
    new_min_value_index = monthly_change_list.index(min_value) + 1  #Adding one to match date with change
    #print(new_min_value_index)
    print(f'Greatest Increase in Profits {date[new_max_value_index]} ${max_value}')
    print(f'Greatest Decrease in Profits {date[new_min_value_index]} ${min_value}')
    
 
dashbreak = "-------------------------"
f = open("Results_output.txt", "w")    
print(("Financial Analysis"), file = f)
print((dashbreak), file= f)
print((f'Total number of months: {total_months}' ), file = f)
print((dashbreak), file =f)
print((f'Total Sum: ${total_sum}'),file=f)
print((f'Average Change: ${average_change}'),file=f)
print((f'Greatest Increase in Profits {date[new_max_value_index]} ${max_value}'),file=f)
print((f'Greatest Decrease in Profits {date[new_min_value_index]} ${min_value}'),file=f)

f.close()
    