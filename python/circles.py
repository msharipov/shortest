import itertools as it
import sympy.geometry as spg
import sys

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} DEPTH")
    exit(1)

MAX_DEPTH = int(sys.argv[1])
circles = {spg.Circle(spg.Point2D(0, 0), 1), spg.Circle(spg.Point2D(1, 0), 1)}
points = {spg.Point2D(0, 0), spg.Point2D(1, 0)}
points |= set(spg.intersection(list(circles)[0], list(circles)[1]))
steps = []
SHORTEST = 1.0
shortest_steps = []
shortest_pair = list(points)


def check(depth):
    global MAX_DEPTH, circles, points, steps, SHORTEST
    global shortest_steps, shortest_pair

    print(f"{depth}/{MAX_DEPTH}", points)
    if (depth == MAX_DEPTH):
        for p1, p2 in it.combinations(points, 2):
            if (p1.distance(p2) < SHORTEST):
                shortest_steps = steps.copy()
                SHORTEST = p1.distance(p2)
                shortest_pair = (p1, p2)
        return

    for p1, p2 in it.permutations(points, 2):
        new_points = set()
        new_circle = spg.Circle(p1, p1.distance(p2))
        if (new_circle in circles):
            continue
        for circle in circles:
            for point in spg.intersection(circle, new_circle):
                new_points.add(point)
        new_points -= points

        circles.add(new_circle)
        points |= new_points
        steps.append((p1, p2))
        check(depth + 1)
        circles.remove(new_circle)
        points -= new_points
        steps.pop()


check(2)
print("\n", shortest_pair, float(SHORTEST))
print(shortest_steps)
