points = [(1,8),(3,4),(8,9),(7,5),(1,47),(10,10)]


def euclideanDistance(point1 ,point2):
    d = (((point2[0] - point1[0])*2 + (point2[1] - point1[1])**2))** (1/2)
    return d

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)


print("Minimum mesafe:", min_distance)
