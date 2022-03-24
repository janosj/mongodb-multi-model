mgeneratejs owners.json -n 10000 | mongoimport --db=JOINS --collection=owners

mgeneratejs animals.json -n 10000 | mongoimport --db=JOINS --collection=animals

