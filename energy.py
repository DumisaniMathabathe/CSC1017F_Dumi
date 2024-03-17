# Question 4
# energy.py
# Program to input the values of the integer numbers m and c, then

# Input values for m and c
m_str = input("Enter the value of m: ")
c_str = input("Enter the value of c: ")

# Convert input strings to integers
m = int(m_str)
c = int(c_str)

# Calculate energy using the provided equation
energy = m * c**2

# Print the result
print("The value of energy, E, is:", energy)

