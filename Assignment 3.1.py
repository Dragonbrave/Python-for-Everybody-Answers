# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked
# above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input("Enter Hours:")
h = float(hrs)
rates=input("Enter Rate:")
rate=float(rates)
if h<=40:
    total=h*rate
    print(total)
else:
    total=40*rate+(h-40)*1.50*rate
    print(total)