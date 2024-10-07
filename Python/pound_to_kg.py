# Code to convert weight from pound to kilograms

weight = eval(input('What is your weight [in pound]'))
weight_in_kilogram = 0.45 * weight
weight_in_kilogram = round(weight_in_kilogram, 2)
print("Your weight is: ", weight_in_kilogram, "kg")
