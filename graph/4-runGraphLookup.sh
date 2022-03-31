source ../demo.conf

mongosh $MDB_CONNECT_URI --eval '

db=db.getSiblingDB("DEMO")

db.collaboration.aggregate([

{
   $graphLookup: {
      from: "collaboration",
      startWith: "$collaborators",
      connectFromField: "collaborators",
      connectToField: "personID",
      as: "widerCircle",
      maxDepth: 1,
      depthField: "depth"
   }
},
{ $out: "graphAnalysis" }

])

'

