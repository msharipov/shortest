import itertools as it
import sympy.geometry as spg
import sys

if (len(sys.argv) != 2):
    print(f"Usage: {sys.argv[0]} DEPTH")
    exit(1)

MAX_DEPTH = sys.argv[1]
circles = set()
points = {spg.Point2D(0, 0), spg.Point2D(1, 0)}
steps = []
SHORTEST = 1.0
shortest_steps = []


def check(depth):
    global MAX_DEPTH, circles, points, steps, SHORTEST, shortest_steps

    for p1, p2 in it.permutations(points, 2):
        if (p1.distance(p2) < SHORTEST):
            shortest_steps = steps
            SHORTEST = p1.distance(p2)

    if (depth == MAX_DEPTH):
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
        if (len(new_points) == 0):
            continue
        circles.add(new_circle)
        points += new_points
        steps.append((p1, p2))
        check(depth + 1)
        circles.remove(new_circle)
        points -= new_points
        steps.pop()


check(0)
print(SHORTEST)
print(shortest_steps)
