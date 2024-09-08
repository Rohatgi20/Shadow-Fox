# Given values
distance_meters = 490  
time_minutes = 7      
# Convert time from minutes to seconds
time_seconds = time_minutes * 60  # 1 minute = 60 seconds

# Calculate speed in meters per second
speed_meters_per_second = distance_meters / time_seconds

# Print the speed without any decimal point
print(int(speed_meters_per_second))
