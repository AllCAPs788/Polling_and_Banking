import statistics

import os
import csv
#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
budget_data = os.path.join('..', 'Python-Challenge', 'budget_data.csv')
# # Method 1: Plain Reading of CSV files
with open(budget_data, 'r') as file_handler:
    lines = file_handler.read()
    csvreader = csv.reader(budget_data, delimiter=',')
    header = next(csvreader)
    print(lines)
    print(type(lines))











#header = nextcsv, skip headers to get to data 

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    
    
    Date = str(lines[0])
    Profits_Losses = int(lines[1])
    print(Date)
    Total = 86

    #PL_average = Profits_Losses/Total
    #month_counter = 0
    #months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    return float(statistics.mean(Profits_Losses))
    #for row in csvreader:
print(print_percentages)
#Your task is to create a Python script that analyzes the records to calculate each of the following:

    #loop syntax: for date in date, for x in Profit, for x in Losses
    #
#The total number of months included in the dataset
    #define months, months = 
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

# If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    #if loss_percent > 50:
     #   type_of_wrestler = "Jobber"
    #else:
     #   type_of_wrestler = "Superstar"

 # Loop through the data
    

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #if name_to_check == row[0]:
            #print_percentages(row)

  