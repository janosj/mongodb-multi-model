source ../demo.conf

mongoimport $MDB_CONNECT_URI --db=DEMO --collection=collaboration --file=enrichedDataSet-final.json

