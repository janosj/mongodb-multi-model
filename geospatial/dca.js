db = db.getSiblingDB('GEO');
cursor = db.airports.find(
  {
      geometry: {
          $nearSphere: {
              $geometry: {
                  type : "Point",
                  coordinates : [-77.0402, 38.8512]
              },
              $maxDistance: 50000
          }
      },
      type: {$in: ["medium_airport", "large_airport"]}
  },
  {
      _id: 0,
      name: 1,
      type: 1,
  }
);
while ( cursor.hasNext() ) {
  printjson( cursor.next() );
}


