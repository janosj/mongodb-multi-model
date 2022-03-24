db = db.getSiblingDB('GEO')
db.airports.createIndex({geometry: "2dsphere"})
db.countries.createIndex({geomtery: "2dsphere"})
