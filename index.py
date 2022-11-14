import re

# Read the contents of index.txt file
file = open("index.txt", "r")

# Loop through each line of the index.txt file
# Store the strings after each space (\s) in each line
requirements = []
for line in file:
    requirements.append(re.split("\s", line))

# Checking the education level by specifying the index

if (requirements[3][0] == "Education:"):
    if(requirements[3][1] == "Diploma"):
        print("Diploma Found.")
    else:
        print("Diploma Not Found.")
else:
    print("Education was not found.")

print(requirements)