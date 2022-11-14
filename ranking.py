import pandas as pd

cv_df = pd.read_csv("cv.csv")
# print(cv_df.head())

i = 0
status = []
while(i < len(cv_df)):
    if(cv_df.Age[i] > 50):
        status.append("Rejected")
        i+=1
        continue;

    if(cv_df.Age[i] < 27):
        if(cv_df.Skills[i] > 4):
            if(cv_df.Education[i] == "Diploma"):
                status.append("On Hold")
            if(cv_df.Education[i] == "Bachelors"):
                status.append("Prospect")
            if (cv_df.Education[i] == "Masters"):
                status.append("Approved")
        elif(cv_df.Experience[i] == 1):
            status.append("Approved")
        else:
            if (cv_df.Education[i] == "Diploma"):
                status.append("Rejected")
            if (cv_df.Education[i] == "Bachelors"):
                status.append("On Hold")
            if (cv_df.Education[i] == "Masters"):
                status.append("Prospect")
    elif(cv_df.Experience[i] == 1):
        if (cv_df.Education[i] == "Diploma"):
            status.append("On Hold")
        if (cv_df.Education[i] == "Bachelors"):
            status.append("Prospect")
        if (cv_df.Education[i] == "Masters"):
            status.append("Approved")
        if (cv_df.Education[i] == "PhD"):
            status.append("Approved")
    elif(cv_df.Skills[i] > 4):
        status.append("Prospect")
    else:
        if (cv_df.Education[i] == "Diploma"):
            status.append("Rejected")
        if (cv_df.Education[i] == "Bachelors"):
            status.append("On Hold")
        if (cv_df.Education[i] == "Masters"):
            status.append("Prospect")
        if (cv_df.Education[i] == "PhD"):
            status.append("Prospect")
    i+=1

print(status)