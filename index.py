import json
import math

# Open and read the JSON file
with open('coordinates.json', 'r') as file:
    data = json.load(file)

def convertToSphericalCoordinates(coordinate):
    return {
        "phi": coordinate["lat"]*math.pi/180,
        "theta": coordinate["lng"]*math.pi/180,
        "rho": 60 # Earth radius, any value will work
    }

sphericalCoordinates = list(map(convertToSphericalCoordinates, data["customCoordinates"]))

print(sphericalCoordinates)