# Create a list of friends' names
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Create a list of tuples with each friend's name and the length of the name
friends_name_length = [(name, len(name)) for name in friends]

# Print the list of tuples
print(friends_name_length)
