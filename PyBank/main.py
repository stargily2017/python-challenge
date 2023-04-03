import os
import csv

PyBank_csv = os.path.join("budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

# create the lists of each data

date = []
# list as total profit loss
profit_loss = []
# m_change as monthly change
m_change = []

# initialise the required variable
# initializing total number of months
number = 0
# initialising total profit-losses
total_pl = 0
# initialising total change profit-losse
total_change_pl = 0
# initialising initial profit
initial_p = 0
# open and read csv file
with open(PyBank_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    previous_net = int(first_row[1])
    
    # looping to find the total profit calculations
    for line in csv_reader:

        number += 1
        date.append(line[0]) 
        profit_loss.append(int(line[1]))
        total_pl += int(line[1])
        # end profit is the final profit and calculate the average change in profit

        #end_p = int(line[1])
        # monthly change profit
        #m_to_m_profit = end_p - initial_p
        # create the list
        #m_change.append(m_to_m_profit)

        #total_change_pl = total_change_pl + m_to_m_profit
        #initial_p = end_p
        net_change = int(line[1]) - previous_net
        previous_net = int(line[1])
        m_change += [net_change]
        
#Average_profit = total_change_pl / (number - 1)
Average_change = sum(m_change) / len(m_change)

greatest_increase = max(m_change)
greatest_decrease = min(m_change)
    
increase_date = date[m_change.index(greatest_increase)]
decrease_date = date[m_change.index(greatest_decrease)]


output = (
    f"Total Months:  {number}\n"
    f"-------------------------\n"
    f"Total:  ${total_pl}\n"
    f"Average Change: ${Average_change:.2f})\n"
    f"-------------------------\n"
    f"Greatest Increase in Profits: {increase_date} ($ ({greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} ($ ({greatest_decrease})\n" 
) 
print(output)
 # Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
 