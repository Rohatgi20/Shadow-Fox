# Given values
radius = 84  # radius of the pond in meters
pi = 3.14    # value of π
water_per_square_meter = 1.4  # liters of water per square meter

# Calculate the area of the pond
pond_area = pi * (radius ** 2)

# Calculate the total amount of water in the pond
total_water = pond_area * water_per_square_meter

# Print the total amount of water without any decimal point
print(int(total_water))
