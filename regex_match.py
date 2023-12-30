import re

string = "white"
pattern = r'white'

match = re.match(pattern, string)

if match:
     print("Match found:", match.group())
else: 
    print("Match not found")