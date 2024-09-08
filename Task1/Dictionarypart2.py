your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each person
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Determine who spent more
if your_total > partner_total:
    spender = "You"
else:
    spender = "Your partner"

print(f"{spender} spent more money overall.")

# Find category with the biggest difference
max_difference = 0
diff_category = None
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses.get(category, 0))
    if difference > max_difference:
        max_difference = difference
        diff_category = category

# Print the category with the biggest difference
if diff_category:
    print(f"The biggest difference in spending is in {diff_category}. You spent ${your_expenses[diff_category]}, while your partner spent ${partner_expenses.get(diff_category, 0)}.")
else:
    print("There are no significant differences in spending categories.")

# Print total expenses for each person
print(f"Your total expenses: ${your_total}")
print(f"Your partner's total expenses: ${partner_total}")