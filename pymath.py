

def square(number):
    result =  number * number
    return result

def cube(number):
    result = number * number * number
    return result

def power (number: int, power_: int) :

    num = number

    if power_ == 0:
        return 0

    if power_ < 0:
        return None

    for i in range(power_ - 1):
        number = number * num

    return number

def root (number: int, root: int = 2):
    num = 0
    while True:
        num += 1
        if power(num, root) == number:
            return num

class geometry():
    # 2d shapes
    class square():
        def area(side):
            result =  side * side
            return result
    class rectangle():
        def area (l, b):
            result = l * b 
            return result
    class triangle():
        def area (base, height):
            result = (base * height) / 2
            return result
        def hypotenuse (s1, s2):
            res = square(s1) + square(s2)
            result = root(res)
            return result
    class circle():
        def area (r):
            result = (22/7) * r * r 
            return result 
        def circumference(r):
            result = 2 * (22/7) * r 
            return result
        def diameter(r):
            result = r * 2
            return result 
        def radius(d):
            result = d / 2
            return result 
        def distance_of_chord_and_center(r, lenghtOfChord):
            loc = lenghtOfChord / 2
            res = square(r) - square(loc)
            result = root(res)
            return result 
        def lenghtOfChord(distanceOfChordFromCenter, radius):
            l = distanceOfChordFromCenter
            r = radius
            res = square(r) - square(l)
            result = root(res) * 2
            return result

    # 3d shapes
    class cube():
        def volumn(side: float):
            result = side * side * side
            return result 
        def area (side: float):
            result = 6 * side * side
            return result 

    class cuboid():
        def volumn (l, b, h):
            result = l * b * h
            return result
        def area (l, b, h):
            result = 2 * ((l*b)+(b*h)+(h*l))
            return result
    
    class cylinder():
        def volume (r, h):
            result = (22/7) * r * r * h
            return result
        def curved_surface_area (r, h):
            result = 2 * (22/7) * r * h 
            return result
        def total_surface_area (r, h):
            result = ( 2 * (22/7) ) * r * (r + h)
            return result
        def capacity(): pass




    

