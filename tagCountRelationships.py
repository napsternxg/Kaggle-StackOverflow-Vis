'''
This python script is used for creating the neccesary files required for creating the top tag relationship visualization which can be seen at ./Submission/topTagRelations.html

The file: TagsRelationshipCount.csv is required for building the support files.
TagsRelationshipCount.csv has been created by running the following query on data.stackexchange.com for the site StackOverflow
Query: select Tags, count(*) as Counts from Posts Group by Tags Order by Counts desc
Once the query finishes click on Download CSV to download the file.

Now copy the file to the directory where this script recides and rename it to TagsRelationshipCount.csv

Configuration options:
Number of Top Tags: topNum

Files Created:
* tagCounts.json - contains the total post count for each tag.
* tagRelations.json - contains the tag relation counts for each tag and the tags which occur with them.
* matrix.json - creates the matrix required for the chord visualization for topNum number of tags.
* topTags.csv - creates a name of topNum number of top tags. Required for chord visualization
'''

import csv
import re
import json
from collections import OrderedDict

tagsList = dict()
totalCounts = dict()
with open('TagsRelationshipCount.csv', 'rb') as csvfile:
        fileText = csv.reader(csvfile)
        i = 0
        fileText.next() # Skip first row which contains header
        fileText.next() # Skip next row which contains post count for no tags
        for row in fileText:
                tagDict = dict()
                tags = row[0].split("><") # Tags are saved in this format <tag1><tag2>
                tags = [re.sub(r'[<>]', "", x) for x in tags] # Gets the simple tag names
                tagDict = {x:int(row[1]) for x in tags} # Creates dictionary with tagname: postcount, will be same for all tags in a row
                for k in tagDict.keys():
                        if not tagsList.has_key(k): # Check required for incrementing non existing key
                               tagsList[k] = dict()
                        for k2 in tagDict.keys():
                                if not tagsList[k].has_key(k2):
                                        tagsList[k][k2] = tagDict[k2]
                                else:
                                        # Increments the current tag count with the new value for the 2 tag pairs
                                        tagsList[k][k2] = tagsList[k][k2] + tagDict[k2]
                        # Simultaneously also create a totalTagCount Dictionary for each tag which will be used for finding top tags
                        if not totalCounts.has_key(k):
                            totalCounts[k] = sum(tagDict.values())
                        else:
                            totalCounts[k] = totalCounts[k] + sum(tagDict.values())

with open('tagCounts.json', 'wb') as fp:
    # Ordered Dict is used to sort the dictionary
    od = OrderedDict(sorted(totalCounts.items(), key=lambda t: t[1], reverse=True))
    json.dump(od, fp, indent=4)

with open('tagRelations.json', 'wb') as fp:
    sortedTags = OrderedDict()
    for k in od.keys():
        # Sort the tag relations using keys of the sorted totalCounts dictionary(od) in decreasing order of post count.
        sortedTags[k] = tagsList[k]
    json.dump(sortedTags, fp, indent=4)

with open('matrix.json', 'wb') as fp:
    topNum = 20 # Edit this value to create the data for different number of top tags
    topTags = [] # Store the list of top tags
    iterD = od.iterkeys() # Used for iterating over the dictionary
    #create a black topNum X topNum matrix having count for each tag pair
    matrix = [[0 for y in range(topNum)] for x in range(topNum)]
    for i in range(topNum):
        k = iterD.next() # Get the next key in the ordered dictionary od
        topTags.append(k) # Add this tag to topTags        
        print k, od[k]
    
    # Update the matrix with the values which denote the count between each tag pair
    for i in range(topNum):
        for j in range(topNum):
            if i != j and sortedTags[topTags[i]].has_key(topTags[j]):
                # Only update if the tag is not itself and the key topTags[j] exits in the dictionary for topTag[i]
                print "sortedTags[%s][%s]" %(topTags[i], topTags[j])
                matrix[i][j] += sortedTags[topTags[i]][topTags[j]]

    json.dump(matrix, fp, indent=4)

with open('topTags.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["name"]) # Write the first row as name of the column
    for tag in topTags:
        writer.writerow([tag]) # Write the tag name as only entry in each row. [tag] is used to print it as string rather than comma separated list of charecters in tag
