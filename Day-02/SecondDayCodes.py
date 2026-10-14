#Inches to Centimetres

# def inch_to_cm(inch):
#     return inch * 2.54

# n =int(input("Enter no in inches: "))

# print(f"No in centimetres is {inch_to_cm(n)}")

# Degrees to farhenheit

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter Temp in Farhenheit: "))
c =f_to_c(f)

print(f"{round(c ,2)} Degree C")