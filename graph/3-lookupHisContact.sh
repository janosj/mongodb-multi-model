source ../demo.conf

mongosh $MDB_CONNECT_URI --eval '

db=db.getSiblingDB("DEMO")

db.collaboration.findOne( {personID: "16258"} )

'

