from statistics import mean

import os
import csv

budget_data = os.path.join('Resources','budget_data.csv')

with open(budget_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')


    header = next(csvreader)
    Month_Counter = 0
    Month_diff= []
    #first_row = next(csvreader)
    Last_month = None
    Last_PL = None
    PL_diff = []
    for row in csvreader:

    #Profits_Losses = []
        Month_Counter = Month_Counter+1 
        Date = row[0] 
        Profits_Losses = (row[1])
        if Last_month!=None:
             
            Month_diff.append(float(Profits_Losses)- float(Last_PL))
        Last_month = Date
        Last_PL = Profits_Losses
        PL_diff.append(float(Profits_Losses)) 
        #first_row = next(csvreader)
        #Profits_Losses.append(next(row[1]))
       # Difference = []
    print(Month_diff)
    print(Month_Counter)
        
        #Profits_Losses = int(row[1])
        
        #Profits_Losses.append(row[1]) 
        #Difference = (row[1] - next(row[1])    
        #Difference.append(next(row[1]) - row[1])
   #look up syntax for specifying list values
    Increase_Month = max(Month_diff)
    Max_month = Month_diff.index(Increase_Month)
    #Increase = Month_diff[Increase_Month]
    #Increase_Month = max(Month_diff,key=Month_diff.get)
    
    print(Increase_Month) 
    #print(Increase)
    Decrease_Month = max(Month_diff)
    Min_month = Month_diff.index(Decrease_Month)
        
    print(Decrease_Month)
    Profits_Total = sum(PL_diff) #needs work 
    Dif_average = round(mean(Month_diff),2) #correct 
   
    print(Dif_average) #correct
    print(Profits_Total)
    #print(Increase_Month)
    #print(Decrease)
    
    Budget_Analysis = os.path.join('Analysis','Budget_Analysis.txt')
    with open(Budget_Analysis, 'w') as results_file:
    #results_file = open("Budget_Analysis.txt", "w")
        results_file.write(
            f"There are {Month_Counter} months:\n" 
            f"The net total amount of 'Profit/Losses' is {Profits_Total} for the budget:\n" 
            f"The Profit/Loss average is {Dif_average} for the budget:\n" 
            f"The largest increase is {Increase_Month} for the budget:\n" 
            f"The largest decrease is {Decrease_Month} for the budget:")
    #text_file.close() 








    
     # consult dicitionaries, key pairs, and https://realpython.com/iterate-through-dictionary-python/ 
#header = nextcsv, skip headers to get to data     
    #print(header)
        #for row in csvreader:
        #print(row[0]) # prints the entire row
        #print(f'First column value: {row[0]}') # prints only first column value for each row 
