# Input number of points
n = int(input("Enter the number of points: "))
points = []
for i in range(n):
    x = float(input(f"Enter x for point {i+1}: "))
    y = float(input(f"Enter y for point {i+1}: "))
    points.append((x, y))

if n < 2:
    print("Need at least two points.")
else:
    x0, y0 = points[0]
    x1, y1 = points[1]
    collinear = True
    for i in range(2, n):
        x, y = points[i]
        if (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
            collinear = False
            break
    if collinear:
        print("The points form a straight line.")
    else:
        print("The points do NOT form a straight line.")
