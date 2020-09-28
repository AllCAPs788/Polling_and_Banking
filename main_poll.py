#Import statistics
import os
import csv
#refer to wrestler functions and how to read/write exercises
# Path to collect data from the Resources folder
election_data = os.path.join('Resources','election_data.csv')

 # Split the data on commas
with open(election_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

    
    #print(header)
    header = next(csvreader)
    for row in csvreader:
        print(row[0]) # prints the entire row
        #print(f'First column value: {row[0]}') # prints only first column value for each row 


     # A complete list of candidates who received votes
     #Candidates() = str("Corey","Khan","Li")    

  # The percentage of votes each candidate won: Candidate_Percent = vote_number/vote_cast
  # print('{}: {}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))
#* The total number of votes each candidate won: vote_cast
# The winner of the election based on popular vote.
# The total number of votes cast: vote_total = sum

# #list of F-statements that will be exported to analysis file
#for printing to Poll_Analysis.txt
# The total number of votes cast (F-statement)
# A complete list of candidates who received votes (F-statement)
# The percentage of votes each candidate won (F-statement)
# 


# fine the function and have it accept the 'wrestler_data' as its sole parameter
#def print_percentages(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    
    #County() = str(election_data[1])
    #votes = int(election_data[0])
    
    #vote_cast = sum(1 for votes in election_data.csv)  # fileObject is your csv.reader


#print(vote_cast)

#text_file = open("Output.txt", "w")

#text_file.write("Candidate_Percent:", "vote_total" " 'TotalAmount')

#text_file.close()