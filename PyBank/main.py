import statistics
import os
import csv

def bank_stats(budget_data):    
    Profits_Losses = []
    Month_Counter = 0 
    for row in budget_data:
        Date = row[0] 
        Month_Counter = Month_Counter+1 
        Profits_Losses.append(int(row[1]))  
        
    Increase = max(Profits_Losses)
    Decrease = min(Profits_Losses)
    Profits_Total = sum(Profits_Losses)
    PL_average = float(statistics.mean(Profits_Losses))   
    
    print(Month_Counter)
    print(Profits_Total)
    print(PL_average)
    print(Increase)
    print(Decrease)

    text_file = open("Budget_Analysis.txt", "w")
    text_file.write(f"There are {Month_Counter} months:]\n" "The net total amount of 'Profit/Losses' is {Profits_Total} for the budget:\n" "The Profit/Loss average is {PL_average} for the budget:\n" "The largest increase is {Increase} for the budget:\n" "The largest decrease is {Decrease} for the budget:")
    text_file.close() 


#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
budget_data = os.path.join('Resources','budget_data.csv')

 # Split the data on commas
with open(budget_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

#header = nextcsv, skip headers to get to data     
    #print(header)
    header = next(csvreader)
    for row in csvreader:
        print(row[0]) # prints the entire row
        print(f'First column value: {row[0]}') # prints only first column value for each row 


        bank_stats(csvreader)


    
     
