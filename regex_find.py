import re

string = "The hair was white in colour"
pattern = r"white"
search = re.search(pattern,string)

if search:
    print(f"The {pattern} found in string")
else:
    print(f"The {pattern} not found in string")
