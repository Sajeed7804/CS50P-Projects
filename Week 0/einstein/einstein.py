# Defining speed of light
c = 300000000

# Prompting user for mass in kg and convert it to an integer
m = int(input("Enter mass in kilograms: "))

# Calculating the energy in Joules using E = mc^2
E = m * c**2

# Printing the energy as an integer
print("The equivalent energy is", int(E), "Joules")
