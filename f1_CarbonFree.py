import math


# define a function to find the key given its value
def find_key(myvalue, mydict):
    for key , value_dic in mydict.items():
        if value_dic == myvalue:
            return key
    return None

# define a function to calculate the distance between two points
def distance(lat1, lon1, lat2, lon2):
    # convert degrees to radians
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    # apply the Harvesine formula to calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c # 6371 is the radius of the Earth in km
    return distance


# define a function to find the nearest neighbor to a given point (lat, lon)
def nearest_neighbor(lat, lon, points):
    min_distance = float('inf') # initialize min_distance with infinity
    nearest_neighbor = None
    for point in points.values():
        d = distance(lat, lon, point[0], point[1])
        if d < min_distance:
            min_distance = d
            nearest_neighbor = point
    return nearest_neighbor


# define a dictionary in which every circuit place is associated to its coordinates
points = {
    "Bahrain": (26.0347, 50.5089),
    "Saudi Arabia": (21.6334, 39.1035),
    "Australia": (-37.8490, 144.9680),
    "Azerbaijan": (40.4083, 49.8622),
    "Miami": (25.9566, -80.2310),
    "Imola": (44.3447, 11.7155),
    "Monaco": (43.7347, 7.4197),
    "Spain": (41.5728, 2.2661),
    "Canada": (45.5079, -73.5290),
    "Austria": (47.2183, 14.7606),
    "Great Britain": (52.0786, -1.0169),
    "Hungary": (47.5106, 19.2556),
    "Belgium": (50.4373, 5.9750),
    "Netherlands": (52.3744, 4.5397),
    "Monza": (45.6237, 9.2844),
    "Singapore": (1.2931, 103.8550),
    "Japan": (34.8414, 136.8550),
    "Qatar": (25.4861, 51.4523),
    "Cota": (30.1375, -97.6400),
    "Mexico": (19.4052, -99.0930),
    "Brazil": (-23.7010, -46.6980),
    "Las Vegas": (36.1068, -115.1600),
    "Abu Dhabi": (24.4749, 54.6038) 
}


# use the nearest neighbor algorithm to find the shortest path through the points
total_distance = 0 # initialize total_distance
current_point = points["Bahrain"] # start at first point
point_path = [current_point] # add the first point to the path
circuit_path = ["Bahrain"]
points.pop("Bahrain") # remove the first point from the list of points

while (len(points)) > 0: # repeat until all points have been visited
    next_point = nearest_neighbor(current_point[0], current_point[1], points) # find the nearest neighbor to the current point

    associated_key = find_key(next_point,points)

    point_path.append(next_point) # add the coordinates of the nearest neighbor to the path
    circuit_path.append(associated_key) # add the circuit name of the nearest neighbor to the path
    points.pop(associated_key) # remove the nearest neighbor from the list of points
    
    total_distance += distance(current_point[0], current_point[1], next_point[0], next_point[1]) # add the distance to the total distance
    current_point = next_point # update the current point

# print the order of the points in the path
print("Order of race tracks:")
for circuit in circuit_path:
    print(circuit)


# print the total distance
print("Total distance: %.2f kilometers" % total_distance)