import math

def math_functions():
    print("basic functionalities of math module: ")

# square root 

number = int(input("enter any number:"))
square_value =math.sqrt(number)
print(f"the square root of {number} is {square_value}")

base= int(input("enter any base:"))
exponent= int(input("enter any exponent"))
exp_value= math.pow(base,exponent)
log_value= math.log(exp_value,base)

print(f"{base} raised to the power of{exponent} is {exp_value} ")

angle_degree = int(input("enter any angle:"))
angle_radians = math.radians(angle_degree)
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)


print(f"sin of {angle_radians} is {sin_value}")
print(f"cos os {angle_radians} is {cos_value}")
print(f"tan of {angle_radians} is {tan_value}")






