import re

# Read the contents of index.txt file
userinput = input('Enter your CV file name: ')
file = open(userinput, "r")

# Loop through each line of the index.txt file
# Store the strings after each space (\s) in each line
status = []
requirements = []
skills_content = ''
skills_count = 0
count = 0
experience_count = 0
for line in file:
    count += 1
    requirements.append(re.split("\s", line))
    if (count == 5):
        skills_content = line
    if (count > 6):
        experience_count += 1

# Checking the education level by specifying the index
# if (requirements[2][0] == "Age:"):
#     if(int(requirements[2][1]) > 50):
#         print("Old")
#     elif(int(requirements[2][1]) < 27):
#         print("Graduate")
#     else:
#         print("Middle Aged Person")

# if (requirements[3][0] == "Education:"):
#     if(requirements[3][1] == "Diploma"):
#         print("Diploma")
#     elif(requirements[3][1] == "Bachelors"):
#         print("Bachelors")
#     elif(requirements[3][1] == "Masters"):
#         print("Masters")
#     elif (requirements[3][1] == "PhD"):
#         print("PhD")
#     else:
#         print("Education level is Unknown")

# Check how many skills the candidate has in the CV
if (re.findall('Communication', skills_content)):
    skills_count += 1
if (re.findall('Equipment Handling', skills_content)):
    skills_count += 1
if (re.findall('Medical Prep and Clean Up', skills_content)):
    skills_count += 1
if (re.findall('Computer Skills', skills_content)):
    skills_count += 1
if (re.findall('Research', skills_content)):
    skills_count += 1
if (re.findall('Time Management', skills_content)):
    skills_count += 1
if (re.findall('Empathy', skills_content)):
    skills_count += 1
if (re.findall('Conflict Resolution', skills_content)):
    skills_count += 1

# if (skills_count > 4):
#     print('Skilled')
# else:
#     print('Unskilled')

# The Rulings

def isAgeOld():
    if(requirements[2][0] == "Age:"):
        if(int(requirements[2][1]) > 50):
            status.append("Rejected")
            displayResults()
        else:
            checkRanking()
            displayResults()

def checkRanking():
    if(int(requirements[2][1]) < 27):
        if(skills_count > 4):
            if(requirements[3][1] == "Diploma"):
                status.append("On Hold")
            if(requirements[3][1] == "Bachelors"):
                status.append("Prospect")
            if (requirements[3][1] == "Masters"):
                status.append("Approved")
        elif(experience_count > 0):
            status.append("Approved")
        else:
            if (requirements[3][1] == "Diploma"):
                status.append("Rejected")
            if (requirements[3][1] == "Bachelors"):
                status.append("On Hold")
            if (requirements[3][1] == "Masters"):
                status.append("Prospect")
    elif(experience_count > 0):
        if (requirements[3][1] == "Diploma"):
            status.append("On Hold")
        if (requirements[3][1] == "Bachelors"):
            status.append("Prospect")
        if (requirements[3][1] == "Masters"):
            status.append("Approved")
        if (requirements[3][1] == "PhD"):
            status.append("Approved")
    elif(skills_count > 4):
        status.append("Prospect")
    else:
        if (requirements[3][1] == "Diploma"):
            status.append("Rejected")
        if (requirements[3][1] == "Bachelors"):
            status.append("On Hold")
        if (requirements[3][1] == "Masters"):
            status.append("Prospect")
        if (requirements[3][1] == "PhD"):
            status.append("Prospect")

def displayResults():
    print(status)

isAgeOld()