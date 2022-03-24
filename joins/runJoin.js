db = db.getSiblingDB('JOINS')
db.owners.aggregate( [
  { $lookup: { 'from': 'animals', 
               'localField': 'animals',
               'foreignField': '_id', 
               'as': 'owns'
             } },
  { $out: "ownersAndTheirAnimals" }
] )

