import os
import csv
import pandas as pd
import math

#store filepath in a variable
budget_csv = os.path.join('./Resources/budget_data.csv')

#read the budget data csv as a dataframe with the pandas library
df = pd.read_csv(budget_csv)

#create a new column in dataframe that is the difference between row i and row i+1
#this new row is offset and shifted up by 1 row
df["Difference"] = df["Profit/Losses"] - df['Profit/Losses'].shift(1)

#sets starting values for max difference, max difference date, and sum of changes
maxDiff = 0
maxDate = ""
minDiff = 0
minDate = ""

#drops NaN values in the dataframe
df.dropna(how='all')

#iterates through each row of the dataframe comparing variables to determine the 
#largest or smallest change values and dates of those changes
for row in df.values:
    if row[-1] > maxDiff:
        maxDate = row[0]
        maxDiff = round(row[-1])
    if row[-1] < minDiff:
        minDate = row[0]
        minDiff = round(row[-1])

#adds up all values in the Difference column
sum_values = df["Difference"].sum()

#takes the average of difference column and rounds the result to 2 decimal places
average_change = round(sum_values/df.count()[2], 2)

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    #skips the header line and starts data collection at row 2
    header = next(csvreader)

    #sets all starting values and empty lists
    month_count = 0
    net_total = 0

    #iterates through each row adding appropriate values to the counters
    for row in csvreader:
        month_count += 1
        net_total = net_total + int(row[1])

#collection of all necessary data points, formatted, ready to print to terminal and write to new file
summary_string = f"""Financial Analysis
-----------------------
Total Months: {month_count}
Total: ${net_total}
Average Change: {average_change}
Greatest Increase in Profits: {maxDate} (${maxDiff})
Greatest Decrease in Profits: {minDate} (${minDiff})"""

f = open("./Analysis/Analysis_Results.txt", 'w')
f.write(summary_string)

print(summary_string)