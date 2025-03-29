import json
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
matplotlib.use('WebAgg') 
import matplotlib.pyplot as plt

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

def convertSphericalToCartesianCoordinates(coordinate):
    return {
        "x": math.cos(coordinate["phi"]) * math.cos(coordinate["theta"]) * coordinate["rho"],
        "y": math.cos(coordinate["phi"]) * math.sin(coordinate["theta"]) * coordinate["rho"],
        "z": math.sin(coordinate["phi"]) * coordinate["rho"]
    }

cartesianCoordinates = list(map(convertSphericalToCartesianCoordinates, sphericalCoordinates))

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

x = list(map(lambda obj: obj["x"], cartesianCoordinates))
y = list(map(lambda obj: obj["y"], cartesianCoordinates))
z = list(map(lambda obj: obj["z"], cartesianCoordinates))

# Creating plot
ax.scatter3D(x, y, z, color = "green")
plt.title("simple 3D scatter plot")
 
# show plot
plt.show()