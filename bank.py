#Import statistics
import os
import csv
#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
budget_data = os.path.join('Resources','budget_data.csv')

 # Split the data on commas
with open(budget_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

    
    #print(header)
    header = next(csvreader)
    for row in csvreader:
        print(row[0]) # prints the entire row
        #print(f'First column value: {row[0]}') # prints only first column value for each row 

#header = nextcsv, skip headers to get to data 
        def bank_stats(budget_data):
    #Date = row[0]
            Profits_Losses = int(row[1])
            Profits_Total = sum(Profits_Losses)
            Case_count = 86
            PL_average = float(statistics.mean(Profits_Losses))   
    #Months = sum(Date)
    #print(Months)

            # = Profits_Losses/Case_count
            print(PL_average)
            Increase = max(Profits_Losses)
            Decrease = min(Profits_Losses)

print(bank_stats)  
    #text_file = open("Budget_Analysis.txt", "w")

    #text_file.write(f"There are {Months} months:" "The net total amount of 'Profit/Losses' is {PL_Total}:" The Profit/Loss average is {PL_average}:" "The largest increase is {Increase}:" "The largest decrease is {Decrease}))

    #text_file.close() 

    
     
