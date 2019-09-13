# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:41:28 2019

@author: Aalok Devkota
"""

import csv
import os



election_data_csv = os.path.join("../Resources", "election_data.csv")
with open (election_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
    total_votes_cast = sum(1 for row in csvreader)
    #print(f'Total number of votes cast: {total_votes_cast}') 
    
election_data_csv = os.path.join("../Resources", "election_data.csv")
with open (election_data_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvfile)
    
    candidates = []
    for row in csv.reader(csvfile):
        candidate = row[2]
        candidates.append(candidate)
   
    unique_candidates = []
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
            
    #print (unique_candidates)
    
    
    
    Khan_vote_counts = candidates.count(unique_candidates[0])
    #print (Khan_vote_counts)
    
    Correy_vote_counts = candidates.count(unique_candidates[1])
    #print (Correy_vote_counts)    
    
    Li_vote_counts = candidates.count(unique_candidates[2])
    #print (Li_vote_counts)
    
    Tooley_vote_counts = candidates.count(unique_candidates[3])
    #print (Tooley_vote_counts)    
    
    vote_list = []
    vote_list.extend((Khan_vote_counts, Correy_vote_counts, Li_vote_counts, Tooley_vote_counts))
    #print(vote_list) 
    max_value = max(vote_list)
    #print(max_value)
    
    Khan_perc ="{:.3%}".format(vote_list[0]/total_votes_cast)
    #print (Khan_perc)
    
    Correy_perc ="{:.3%}".format(vote_list[1]/total_votes_cast)
    #print (Correy_perc)
    
    Li_perc ="{:.3%}".format(vote_list[2]/total_votes_cast)
    #print (Li_perc)

    Tooley_perc ="{:.3%}".format(vote_list[3]/total_votes_cast)
    #print (Tooley_perc)
   
    new_dict = dict(zip(unique_candidates, vote_list))   
    #print (new_dict)
    
    winner = max(new_dict, key=new_dict.get)
    #print(winner)
dashbreak = "-------------------------"
print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes_cast}")
print(dashbreak)
print(f"{(unique_candidates[0])} {Khan_perc} ({Khan_vote_counts})")
print(f"{(unique_candidates[1])} {Correy_perc} ({Correy_vote_counts})")
print(f"{(unique_candidates[2])} {Li_perc} ({Li_vote_counts})")
print(f"{(unique_candidates[3])} {Tooley_perc} ({Tooley_vote_counts})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)
        
f = open("Results_output.txt", "w")    
print(("Election Results"), file = f)
print((dashbreak), file= f)
print((f"Total Votes: {total_votes_cast}"), file = f)
print((dashbreak), file =f)
print((f"{(unique_candidates[0])} {Khan_perc} ({Khan_vote_counts})"),file=f)
print((f"{(unique_candidates[1])} {Correy_perc} ({Correy_vote_counts})"),file=f)
print((f"{(unique_candidates[2])} {Li_perc} ({Li_vote_counts})"),file=f)
print((f"{(unique_candidates[3])} {Tooley_perc} ({Tooley_vote_counts})"),file=f)
print((dashbreak),file=f)
print((f"Winner: {winner}"),file=f)
print((dashbreak),file=f)   
f.close()