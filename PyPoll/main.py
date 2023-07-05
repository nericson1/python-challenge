import os
import csv
import pandas as pd
import math

#store filepath in a variable
election_csv = os.path.join('./Resources/election_data.csv')

#read the election data csv as a dataframe with the pandas library
df = pd.read_csv(election_csv)

#sets empty counters and dictionaries for future use
total_votes = 0
cand_dict = {}

#collects a list of unique candidate names
candidates = df["Candidate"].unique()

#iterates through the list of candidate names and assigns them as keys with values to the candidate dictionary
for candidate in candidates:
    cand_dict[candidate] = 0

#iterates through each row in the dataframe collecting the total number of votes and 
#assigns each candidate their correct number of votes
for row in df.values:
    total_votes += 1
    candidate = row[2]
    cand_dict[candidate] = cand_dict[candidate] + 1

#determines which candidate in the dictionary had the highest number of votes
winner = max(cand_dict, key = cand_dict.get)

#assigns the keys and values in the candidate dictionary to their own lists
cand_names = list(cand_dict.keys())
cand_votes = list(cand_dict.values())

#divides the candidates votes by the total , multiplying that by 100 to get their percentage of the votes
#then rounds this number to 3 decimal places
charles_percent = round(((cand_votes[0]/total_votes)*100), 3)
diana_percent = round(((cand_votes[1]/total_votes)*100), 3)
raymon_percent = round(((cand_votes[2]/total_votes)*100), 3)

#puts each candidates percentage of votes into a list
total_percents = [charles_percent, diana_percent, raymon_percent]

#collection of all necessary data points, formatted, ready to print to terminal and write to new file
summary_string = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{cand_names[0]}: {total_percents[0]}% ({cand_votes[0]})
{cand_names[1]}: {total_percents[1]}% ({cand_votes[1]})
{cand_names[2]}: {total_percents[2]}% ({cand_votes[2]})
-------------------------
Winner: {winner}
-------------------------"""

f = open("./Analysis/Analysis_Results.txt", 'w')
f.write(summary_string)

print(summary_string)