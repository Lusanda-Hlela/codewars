def point_in_circle(x, y):
    radius = ((x ** 2) + (y ** 2)) ** 0.5
    if radius < 1:
        return True
    else:
        return False