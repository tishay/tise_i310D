def calculate_volume_of_sphere(radius):
    import math
    volume = ((4 / 3)* math.pi * (radius**3))
    return volume

radius1 = 30
area1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a circle with the radius {radius1} is: {area1:.2f}")

radius2 = 40
area2 = calculate_volume_of_sphere(radius2)
print(f"The volume of a circle with the radius {radius2} is: {area2:.2f}")
