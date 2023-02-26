import re

# Define the regular expression pattern
pattern = r'a(b{2,3})'

# Test strings
test_strings = ['ab', 'abb', 'abbb', 'ac', 'abc']

# Loop through the test strings and print whether they match the pattern
for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")
