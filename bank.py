import statistics

import os
import csv
#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
budget_data = os.path.join('Resources','budget_data.csv')
# # Method 1: Plain Reading of CSV files
 # Split the data on commas
with open(budget_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(csvreader)
#header = nextcsv, skip headers to get to data 
def bank_stats(budget_data):
    Date = str(budget_data[0])
    Profits_Losses = float(budget_data[1])
    Total = 86
    print(Date)

    
bank_stats  
    
    #print(Date)
    

    #PL_average = Profits_Losses/Total
    #month_counter = 0
    #months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    #return float(statistics.mean(Profits_Losses))
    #for row in csvreader:
#print(print_percentages)
#Your task is to create a Python script that analyzes the records to calculate each of the following:

    
#The total number of months included in the dataset
    #define months, months = sum(Date)
#The net total amount of "Profit/Losses" over the entire period
    #sum of Profit, sum of Profit/Losses   
# The average of the changes in "Profit/Losses" over the entire period
    # PL/Total, Total = 86
#The greatest increase in profits (date and amount) over the entire period
    #=profits/losses.max (whatever function returns max amoutn)
#The greatest decrease in losses (date and amount) over the entire period
    #MIN for profits/losses

#row_count = sum(1 for row in budget_data.csv)  # fileObject is your csv.reader

#Print(Date)


 # Loop through the data
    

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #if name_to_check == row[0]:
            #print_percentages(row)

  #for printing to Budget_Analysis.txt

#list of F-statements that will be exported to analysis file  
#text_file = open("Output.txt", "w")

#text_file.write("Purchase Amount: " 'TotalAmount')

#text_file.close()