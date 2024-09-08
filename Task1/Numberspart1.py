def formatted_string(number, format_specifier):
    # Use the format function to format the number according to the format specifier
    result = format(number, format_specifier)
    return result

# Call the function with the arguments 145 and 'o'
formatted_result = formatted_string(145, 'o')

# Print the result
print(formatted_result)
