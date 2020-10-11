#Py_Bank
#imports
import os
import csv

#Define variables
months = []
profit_changes = []

count_months = 0
net_profit = 0
previous_month_profit = 0
current_month_profit = 0
profit_change = 0

# folder path 
csvpath = os.path.join("..","Resources", "budget_data.csv")


# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
             
    #for loop to loop through rows
    for row in csvreader:

        # Count months
        count_months += 1

        # Net total over the entire period
        current_month_profit = int(float(row[1]))
        net_profit += current_month_profit

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit = current_month_profit
            continue

        else:

            # Calculate profit change 
            profit_change = current_month_profit - previous_month_profit

            # Add to months list
            months.append(row[0])

            # Add to profit changes list
            profit_changes.append(profit_change)

            # Prep for the next loop
            previous_month_profit = current_month_profit

    #sum and average of changes in "Profit/Losses"
    sum_profit = sum(profit_changes)
    average_profit = round(sum_profit/(count_months - 1), 2)

    # greatest increase and decrease in "Profit/Losses"
    greatest_increase = max(profit_changes)
    greatest_decrease = min(profit_changes)
    best_month_index = profit_changes.index(greatest_increase)
    worst_month_index = profit_changes.index(greatest_decrease)
    best_month = months[best_month_index]
    worst_month = months[worst_month_index]

# Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${average_profit}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})")


#Export
output_file = os.path.join("Py_Bank.csv")
with open(output_file, "w") as datafile:

    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months:  {count_months}\n")
    datafile.write(f"Total:  ${net_profit}")
    datafile.write(f"Average Change:  ${average_profit}\n")
    datafile.write(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})\n")