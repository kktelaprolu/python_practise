fruits = ['apple','pineapple','orange','banana']

for fruit in fruits:
    if fruit == "orange":
     break
    print(fruit)

toys = ['car', 'bus', 'doll','micky']
for toy in toys:
    if toy == "doll":
     continue
    print(toy)

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if 'ERROR' in line:
      print(line)

count=0
while count<5:
   print(count)
   count+=1

list = [1,2,3,4,5,6]

while len(list)<7:
   print(f"valid")
   break