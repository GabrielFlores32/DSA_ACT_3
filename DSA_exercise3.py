def vowelsToUpper(string):
    #Convert vowels to uppercase, leave other characters unchanged
    return ''.join([char.upper() if char in 'aeiouAEIOU' else char for char in string])

# Sample strings
sample_string = "Dear Gabriel why are you so good looking?"

# Print the result of the sample string
print("Vowels to uppercase:", vowelsToUpper(sample_string))