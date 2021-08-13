weight=float(input("Please enter your weight (Kg) : "))
height=float(input("Please enter your height (m) : "))
BMI=weight/(height**2)
if BMI<18.5 :
    result=" under weight "
if 18.5<BMI<24.9 :
    result=" normal "
if 25<BMI<29.9 :
    result=" over weight "
if 30<BMI<34.9 :
    result=" obese "
if BMI>35 :
    result=" extremely obese "
print(result)