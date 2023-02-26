import re

pattern = r'a(b*)'

test_strings = ['ab', 'abb', 'abbb', 'a', 'ac', 'c']


for string in test_strings:
    match = re.search(pattern, string)
    if match:
        print(f"{string} matches the pattern '{pattern}'")
    else:
        print(f"{string} does not match the pattern '{pattern}'")
