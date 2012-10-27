import csv
import re
import json
from collections import OrderedDict

tagsList = dict()
totalCounts = dict()
with open('TagsRelationshipCount.csv', 'rb') as csvfile:
        fileText = csv.reader(csvfile)
        i = 0
        fileText.next()
        fileText.next()
        for row in fileText:
                tagDict = dict()
                tags = row[0].split("><")
                tags = [re.sub(r'[<>]', "", x) for x in tags]
                tagDict = {x:int(row[1]) for x in tags}
                for k in tagDict.keys():
                        if not tagsList.has_key(k):
                               tagsList[k] = dict()
                        for k2 in tagDict.keys():
                                if not tagsList[k].has_key(k2):
                                        tagsList[k][k2] = tagDict[k2]
                                else:
                                        tagsList[k][k2] = tagsList[k][k2] + tagDict[k2]
                        if not totalCounts.has_key(k):
                            totalCounts[k] = sum(tagDict.values())
                        else:
                            totalCounts[k] = totalCounts[k] + sum(tagDict.values())

with open('tagCounts.json', 'wb') as fp:
    od = OrderedDict(sorted(totalCounts.items(), key=lambda t: t[1], reverse=True))
    json.dump(od, fp, indent=4)

with open('tagRelations.json', 'wb') as fp:
    sortedTags = OrderedDict()
    for k in od.keys():
        sortedTags[k] = tagsList[k]
    json.dump(sortedTags, fp, indent=4)

with open('matrix.json', 'wb') as fp:
    topNum = 20
    topTags = []
    iterD = od.iterkeys()
    matrix = [[0 for y in range(topNum)] for x in range(topNum)]
    for i in range(topNum):
        k = iterD.next()
        topTags.append(k)        
        print k, od[k]
    
    for i in range(topNum):
        for j in range(topNum):
            if i != j and sortedTags[topTags[i]].has_key(topTags[j]):
                print "sortedTags[%s][%s]" %(topTags[i], topTags[j])
                matrix[i][j] += sortedTags[topTags[i]][topTags[j]]

    json.dump(matrix, fp, indent=4)

with open('topTags.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["name"])
    for tag in topTags:
        writer.writerow([tag])
