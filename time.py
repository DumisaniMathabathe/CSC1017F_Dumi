# Program to convert an amount of minutes into an equivalent amount
# of days, hours and minutes.
#
# Name: Stephan Jamieson
#
input_str = input("Enter a quantity of minutes: ")
minutes = int(input_str)

days = minutes//(24*60)

hours = (minutes//60) % 24

minutes %= 60

print("The number of days is", days, end=', ')
print("the number of hours is", hours, end=', ')
print("and the number of minutes is", minutes, end='.' )