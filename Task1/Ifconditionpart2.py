# Define the list of cities for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter the names of two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Function to determine the country of a city
def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

# Get the country for both cities
country1 = get_country(city1)
country2 = get_country(city2)

# Check if both cities belong to the same country
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print("They don't belong to the same country.")
else:
    print("One or both of the cities are not recognized.")
