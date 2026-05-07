# weight converter
# This program converts weights between different units.

weight = float(input("Enter your weight: "))
unit =input("Enter unit (kg or lb): ")

original_weight = weight
original_unit = unit

# if the unit is kg, convert to lb
if unit == "kg":
    weight = weight * 2.20462
    unit = "lb"
elif unit == "lb":
    weight = weight / 2.20462
    unit = "kg"
else: 
    print( f"{unit} is Invalid ")

print(f"{original_weight} {original_unit} is {weight} {unit}")

