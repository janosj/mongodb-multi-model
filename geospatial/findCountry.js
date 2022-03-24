db=db.getSiblingDB('GEO')
current_country = db.countries.findOne({geometry: {$geoIntersects: {$geometry: {type: "Point", coordinates: [-77.0402, 38.8512]}}}});
print('Current country: ' + current_country.name);

