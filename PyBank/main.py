import statistics
import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

with open(budget_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')


    header = next(csvreader)
    first_row = next(csvreader)
    for row in csvreader:

    #Profits_Losses = []
        Month_Counter = 1 
        Profits_Losses = row[1]
        Profits_Losses.append(first_row)
        Difference = []
    
    
        Date = row[0] 
        Profits_Losses = int(row[1])
        Month_Counter = Month_Counter+1 
        Profits_Losses.append(row[1]) 
        #Difference = (row[1] - next(row[1])    
        Difference.append(next(row[1]) - row[1])
   #look up syntax for specifying list values
    #Increase = max(Profits_Losses) 
    #Decrease = min(Profits_Losses)
    
    Profits_Total = sum(Profits_Losses) + int(first_row[1])
    Dif_average = float(statistics.mean(Difference))   
    
    print(Month_Counter)
    print(Profits_Total)
    print(Dif_average)
    #print(Increase)
    #print(Decrease)
    
    Budget_Analysis = os.path.join('Analysis','Budget_Analysis.txt')
    with open(Budget_Analysis, 'w') as results_file:
    #results_file = open("Budget_Analysis.txt", "w")
       results_file.write(
            f"There are {Month_Counter} months:\n" 
            f"The net total amount of 'Profit/Losses' is {Profits_Total} for the budget:\n" 
            f"The Profit/Loss average is {Dif_average} for the budget:\n" 
            f"The largest increase is {Increase} for the budget:\n" 
            f"The largest decrease is {Decrease} for the budget:")
    #text_file.close() 


#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder


# Split the data on commas






    
     # consult dicitionaries, key pairs, and https://realpython.com/iterate-through-dictionary-python/ 
#header = nextcsv, skip headers to get to data     
    #print(header)
        #for row in csvreader:
        #print(row[0]) # prints the entire row
        #print(f'First column value: {row[0]}') # prints only first column value for each row 
