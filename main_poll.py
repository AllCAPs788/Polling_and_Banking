import statistics
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
        
    def Vote_Stats(election_data):
        print(row[0]) # prints the entire row
        #print(f'First column value: {row[0]}') # prints only first column value for each row 
        Candidates() = str("Corey","Khan","Li", "O'Tooley")   
        vote = row[0]
        vote_cast = #The total number of votes each candidate won print('{}: {}% ({})'.format(key,round((key_votes/total_number_votes * 100),3),key_votes))
        vote_total = sum(vote)
        County() = str(election_data[1]) # A complete list of candidates who received votes
        winner = 
        print(Candidates[])
        print(vote)

        #text_file = open("Output.txt", "w")

        #text_file.write(f"Winner: {winner}" "Candidate votes:{candidate votes" "vote percentage:{vote percentage}")
            print(f"Stats for {name}")
    print(f"WIN PERCENT: {str(win_percent)}")
    print(f"LOSS PERCENT: {str(loss_percent)}")
    print(f"DRAW PERCENT: {str(draw_percent)}")
    print(f"{name} is a {type_of_wrestler}")
        #text_file.close()
    # 
  # The percentage of votes each candidate won: Candidate_Percent = vote_number/vote_cast
  

# The winner of the election based on popular vote.
# The total number of votes cast: vote_total = sum

# #list of F-statements that will be exported to analysis file
#for printing to Poll_Analysis.txt
# The total number of votes cast (F-statement)
# A complete list of candidates who received votes (F-statement)
# The percentage of votes each candidate won (F-statement)
# 



    
    
    
    
    




