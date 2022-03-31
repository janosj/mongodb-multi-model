source ../demo.conf

mongosh $MDB_CONNECT_URI --eval '

db=db.getSiblingDB("DEMO")

db.graphAnalysis.findOne( {personID: "21194"} )

'

echo 
echo "Suggestion: that data can be easier to understand when viewed in Compass."
echo "Use { personID: '21194' } as the query filter (on the graphAnalysis collection)."

