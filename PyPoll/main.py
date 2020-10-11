#Py_Poll
#import csv
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")

#define variables
total_votes_cast = 0
list_of_votes=[]
candidates = []
percentage_votes = []
total_votes_by_candidate = []


#for loop to loop through rows
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
    
    #calculate total votes cast
        total_votes_cast+=1
    
    #create list of candidates
        list_of_votes.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
        
    #create list of votes
    list_of_votes.append(row[2])

    for candidate in candidates:
        total_votes_by_candidate.append(list_of_votes.count(candidate))
        percentage_votes.append(round(list_of_votes.count(candidate)/total_votes_cast*100,3))

    winner = candidates[total_votes_by_candidate.index(max(total_votes_by_candidate))]

    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes_cast}')
    print('--------------------------------')
    for x in range(len(total_votes_by_candidate)):
        print(f'{candidates[x]}: {percentage_votes[x]}% {total_votes_by_candidate[x]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')
    print('```')

    # Set variable for output file
output_file = os.path.join("web_final.csv")

    #  Open the output file
with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)

    # Write the output file
        datafile.write('Election Results')
        datafile.write('\n------------------------------------')
        datafile.write(f'\nTotal Votes: {total_votes_cast}')
        datafile.write('------------------------------------')
        for x in range (len(candidates)):
            datafile.write(f'\n{candidates[x]}: {percentage_votes[x]}% {total_votes_by_candidate[x]}')
        datafile.write('\n------------------------------------')
        datafile.write(f'\nWinner: {winner}')
        datafile.write('\n------------------------------------')
