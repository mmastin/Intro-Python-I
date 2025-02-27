# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __repr__(self):
        return f'{self.name}, {self.lat}, {self.lon}'

    def __str__(self):
        return f'{self.name} \n Latitude: {self.lat} \n Longitude: {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __repr__(self):
        return f'{self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}'

    def __str__(self):
        return f'{self.name} \n Difficulty: {self.difficulty} \n Size: {self.size} \
            \n Latitude: {self.lat} \n Longitude: {self.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(name='Catacombs', lat=41.70505, lon=-121.51521)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(name='Newberry Views', difficulty=1.5, size=2,
                lat=44.052137, lon=-121.41556)

print(geocache)
