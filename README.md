# **Election_Analysis**

## **Overview of Project**

### Purpose of Project:
The purpose of this project was to analyze the election results of a local congressional election in Colorado. The data was obtained from the Colorado Board of Elections. Total votes and percentage of votes were evaluated across both candidates and individual counties resulting in identifying a winning candidate and the county that contributed the most votes to the election.

### The Following Tasks Were Completed:
1. Tally of the total number of votes cast.

2. The total number of votes each county contributed. 
3. The percentage of votes each county contributed.
4. The county that contributed the most votes.

5. Compiled a complete list of candidates who received votes.
6. The total number of votes each candidate won. 
7. The percentage of votes each candidate won.
8. The winner of the election based on popular vote.

## **Resources**
* Data Source: election_results.csv
* Software: Python 3.10, Visual Code 1.63

## **Election-Audit Results**
### Total Number of Votes Cast:
* There were a total of 369,711 votes cast in this congressional election.

### Total Number of Votes and the Percentage of Total Votes for Each County:
* Jefferson county cast 10.5% of the total votes with 38,855 votes.
* Denver county cast 82.8% of the total votes with 306,055 votes.   
* Arapahoe county cast 6.7% of the total votes with 24,801 votes.

### County with the Largest Number of Votes:
* Denver had the largest number of votes.

### Candidates Who Received Votes:
* Charles Casper Stockham
* Diana DeGette
* Raymon Anthony Doane

### Candidates Results:
* Charles Casper Stockham received 23.0% of the votes with 85,213 total votes.
* Diana DeGette received 73.8% of the votes with 272,892 total votes.
* Raymon Anthony Doane received 3.1% of the votes with 11,606 total votes.

### Winner of the Election:
* The winner of the election was Diana DeGette who received 73.8% of the votes with 272,892 total votes.

## **Election-Audit Summary**
This script can be modified to count any item by category not just candidates. 

        # If the item to be counted does not match any existing item in the item list:
        if item_name not in item_options:

            # Add the item name to the list.
            item_options.append(item_name)

            # Begin tracking that candidate's voter count.
            item_count[item_name] = 0
      
        # Add a count to that item’s count
        item_votes[item_name] += 1
