#!/usr/bin/env python3

import json
import bson
import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")
db = conn.GRAPH
collection = db.persons
print("Connected to MongoDB")

personDetailsFile = open("4-personDetails-generated.json", "r")
enrichedDataSet = open("enrichedDataSet.json", "w")

priorFromNode = "bogus"
with open("1-dataset-tweaked.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    values = stripped_line.split()
    fromNode = values[0]
    toNode = values[1]
    if fromNode != priorFromNode:
      print("New Record")
      if priorFromNode != 'bogus':
        print("----Inserting record into database")
        newJsonDoc["collaborators"] = friendsList
        print( json.dumps(newJsonDoc) )
        collection.insert_one(newJsonDoc)
        #enrichedDataSet.write( json.dumps(newJsonDoc) )
      priorFromNode = fromNode
      detailsFromFile = personDetailsFile.readline()
      detailsAsJson = json.loads(detailsFromFile)
      newJsonDoc = {}
      friendsList = []
      newJsonDoc["personID"] = fromNode
      newJsonDoc["firstName"] = detailsAsJson["firstname"]
      newJsonDoc["lastName"] = detailsAsJson["lastname"]
    print("Adding friend")
    #friendsList.append( {"personID":toNode}  )
    friendsList.append( toNode )
# Last record gets dropped

conn.close()
personDetailsFile.close()
enrichedDataSet.close()

print("Finished.")

