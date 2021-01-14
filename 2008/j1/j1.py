weightinput = 69
heightinput = 1.73

bmi = weightinput/(heightinput*heightinput)
if bmi > 25:
    print("Overweight")
elif bmi <= 25 and bmi >= 12.5:
    print("Normal Weight")
else:
    print("Underweight")
