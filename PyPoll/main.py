import os 
import csv

elction_file = os.path.join("Resources","election_data.csv")

candidate_votes = {}
candidate_list =[]
vote_count = []
total_votes = 0

with open(elction_file) as csvfile:
     reader = csv.reader(csvfile, delimiter = ',')
     # Reading the header
     header = next(csvfile)

     # Using for loop tho go thru each row in the datafile
     for row in reader:
       
        candidate_name = row[2]
        total_votes = total_votes +1
      
        # Checking name of the candidates if they are same or not
        if candidate_name not in candidate_list:
            # Get unique candidate names
            candidate_list.append(candidate_name)
            # Total number of votes per candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
        # Cheking highest votes for the winner with lambda function
        winner = max(candidate_votes, key = lambda x:x[1])

# Displaying information
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
for key in candidate_votes:
    key, round(((candidate_votes[key]/total_votes) * 100),3)
    print(f'{key}: {round(((candidate_votes[key]/total_votes) * 100),3)}% ({candidate_votes[key]})')
print("-------------------------")
print("The winner: " + winner)
print("-------------------------")


# Printing information to output.txt
textfile = os.path.join("Analysis","analysis.txt")
with open(textfile,"w") as textfile:
    print("Election Results", file=textfile)   
    print("-------------------------", file=textfile)
    print("Total Votes :" + str(total_votes), file=textfile)    
    print("-------------------------", file=textfile)
    for key in candidate_votes:
        key, round(((candidate_votes[key]/total_votes) * 100),3)
        print(f'{key}: {round(((candidate_votes[key]/total_votes) * 100),3)}% ({candidate_votes[key]})', file=textfile)
    print("-------------------------", file=textfile)
    print("The winner: " + winner, file=textfile)
    print("-------------------------", file=textfile)
           
            
                
        







     

