import statistics
import os
import csv

election_data = os.path.join('Resources','election_data.csv')
election_dict = {}
with open(election_data) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')

    
    #print(header)
    header = next(csvreader)
    for row in csvreader:
      Can_counter = row[2]
      if Can_counter in election_dict:
        election_dict[Can_counter] += 1
      else:
        election_dict[Can_counter] = 1
    print(election_dict)
    Max_vote = 0
    Winner_name = None
    Vote_total = sum(election_dict.values()) 
    Results = []
    Results.append("Election Results")
    Results.append("---------------------------------")
    Results.append("Total Votes {}".format(Vote_total))
    Results.append("---------------------------------")
    #vote_percent
    for name, vote_tally in election_dict.items():
      vote_percent = vote_tally/Vote_total
      print(name,vote_tally)
      if Winner_name == None:
        Max_vote = vote_tally
        Winner_name = name
      else: 
        if vote_tally > Max_vote:
          Max_vote = vote_tally
          Winner_name = name
      Results.append('{}: {:.3f}% ({})'.format(name,round((vote_tally/Vote_total * 100),3),vote_tally))
    Results.append("---------------------------------")  
    Results.append("Winner: {}".format(Winner_name))       
    
    print(Max_vote,Winner_name)
    print(Vote_total)
     
    
   
    Poll_Analysis = os.path.join('Analysis','Poll_Analysis.txt')
    with open(Poll_Analysis, 'w') as results_file:
    #   
    # text_file.write(f"Winner: {winner}]\n" "Candidate votes:{candidate votes\n" "vote percentage:{vote percentage}\n")
        for row in Results:    #print(f"Stats for {name}")
            print(row)
            results_file.write(row +"\n")
           
# consult dicitionaries, key pairs, and https://realpython.com/iterate-through-dictionary-python/ 



    
    
    
    
    




