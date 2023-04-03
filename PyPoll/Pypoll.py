import os
import csv

PyPoll_csv = os.path.join("election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# create the list of data

candidate = []
percent_vote = []
total_count_vote = []
unique_person = []
total_vote = 0

# initialising total number of votes
number = 0

with open(PyPoll_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
    for line in csv_reader:
        number += 1
# set candidates in candidate[]
        candidate.append(line[2])
    
    #looping for finding the total number of votes and the percentage of vote for each candidate
    for i in set (candidate):
        unique_person.append(i)
        j = candidate.count(i)
        total_count_vote.append(j)
        k = round((j / number) * 100,2)
        percent_vote.append(k)
        total_vote += j
        
        win_vote = max(total_count_vote)
        win_candidate = unique_person[total_count_vote.index(win_vote)]
        
    
    
          # Generate Output Summary
output = f"Election Results\n"
output += f"----------------------------\n"
output += f"Total votes: {total_vote}\n"
output += f"----------------------------\n"

for p in range(len(set(unique_person))):
    output += f"{unique_person[p]} :({percent_vote[p]}%) {total_count_vote[p]}\n"

output += f"The winner is: {win_candidate}\n"

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)               
