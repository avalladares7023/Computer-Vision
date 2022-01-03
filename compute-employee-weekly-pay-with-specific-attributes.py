"""
Student Name: Aimee Valladares
Purpose: Computing the employee's weekly pay using the hourly wage, number of
         regular hours, and overtime pay
"""

# Get the variables
hourlyWage = float(input("Enter your hourly wage: "))
regularHours = float(input("Enter the total number of regular hours you worked: "))
overtimeHours = float(input("Enter the total number of overtime hours you worked: "))

# Compute the total weekly pay
totalWeeklyPay = (hourlyWage * regularHours + (overtimeHours * hourlyWage * 1.5))

# Print the output
print("Your total weekly pay is $%0.2f" % totalWeeklyPay) # $0.2f % is used for precision
