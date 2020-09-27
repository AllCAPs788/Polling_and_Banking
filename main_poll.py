#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:


#* As an example, your analysis should look similar to the one below:
import os
import csv
#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
election_data = os.path.join('Resources','election_data.csv')
# # Method 1: Plain Reading of CSV files
with open(election_data, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))

    #for vote in votes

     # A complete list of candidates who received votes
  #candidate = str
  # The percentage of votes each candidate won: vote_number/vote_cast
  # print('{}: {}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))
#* The total number of votes each candidate won: vote_cast
# The winner of the election based on popular vote.
# The total number of votes cast: vote_total = sum

# #list of F-statements that will be exported to analysis file
#for printing to Poll_Analysis.txt
# 
# 
# 
# 
# fine the function and have it accept the 'wrestler_data' as its sole parameter
#def print_percentages(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    #Candidates() = str("Corey","Khan","Li")
    #County() = str(election_data[1])
    #votes = int(election_data[0])
    
    #vote_cast = sum(1 for votes in election_data.csv)  # fileObject is your csv.reader


#print(vote_cast)

#text_file = open("Output.txt", "w")

#text_file.write("Purchase Amount: " 'TotalAmount')

#text_file.close()