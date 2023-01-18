import os 
import csv

elction_file = os.path.join("Resources","election_data.csv")

election_data = []
candidate_votes = {}
candidate_list =[]
vote_count = []
percent_vote = []
total_votes = 0

with open(elction_file) as csvfile:
     reader = csv.reader(csvfile, delimiter = ',')
     header = next(csvfile)

     for row in reader:
        # Candiadate info to list
        #election_data.append(row[2])
        candidate_name = row[2]
        #Number  of Votes
        total_votes = total_votes +1
        #print(total_votes)
     
     
        
        if candidate_name not in candidate_list:
            # Get unique candidate names
            candidate_list.append(candidate_name)
            # Total number of votes per candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

      
winner = max(candidate_votes, key = lambda x:x[1])
           
            
                
        



print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
for key in candidate_votes:
    print(key, round(((candidate_votes[key]/total_votes) * 100),3))
print("-------------------------")
print("The winner: " + winner)
print("-------------------------")



     

