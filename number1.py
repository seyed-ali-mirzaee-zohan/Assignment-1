import math
operator=input("Please enter your desired operation : ")
if operator=="sin":
    a=float(input(" Please enter the angle whose Sin you want to find : "))
    result=math.sin(math.radians(a))
if operator=="cos":
    a=float(input(" Please enter the angle whose Cos you want to find : "))
    result=math.cos(math.radians(a))
if operator=="tan":
    a=float(input(" Please enter the angle whose Tan you want to find : "))
    result=math.tan(math.radians(a))
if operator=="cot":
    a=float(input(" Please enter the angle whose Cot you want to find : "))
    result= 1/(math.tan(math.radians(a)))
if operator=="factorial":
    a=float(input(" Please enter your number : "))
    result=math.factorial(a)
if operator=="radical":
    a=float(input(" Please enter your number : ")) 
    result=a**.5
if operator=="+":
    a=float(input("Please enter your first number : "))
    b=float(input("Please enter your second number : "))
    result=a+b
if operator=="-":
    a=float(input("Please enter your first number : "))
    b=float(input("Please enter your second number : "))
    result=a-b
if operator=="*":
    a=float(input("Please enter your first number : "))
    b=float(input("Please enter your second number : "))
    result=a*b
if operator=="/":
    a=float(input("Please enter your first number : "))
    b=float(input("Please enter your second number : "))
    if b==0:
            result=" Continued work is not allowed !! "
    if b!=0:
            result=a/b
print(result)