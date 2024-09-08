# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League
num_members = len(justice_league)
print(f"Number of members: {num_members}")

# 2. Batman recruited Batgirl and Nightwing as new members
justice_league.extend(["Batgirl", "Nightwing"])
print(f"Updated list after adding Batgirl and Nightwing: {justice_league}")

# 3. Move Wonder Woman to the beginning of the list (making her the leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"List after moving Wonder Woman to the front: {justice_league}")

# 4. Move "Green Lantern" in between Aquaman and Flash to separate them
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print(f"List after moving Green Lantern between Aquaman and Flash: {justice_league}")

# 5. Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New list of Justice League members: {justice_league}")

# 6. Sort the Justice League alphabetically and make the hero at the 0th index the new leader
justice_league.sort()
new_leader = justice_league[0]
print(f"Alphabetically sorted list: {justice_league}")
print(f"New leader after sorting: {new_leader}")
