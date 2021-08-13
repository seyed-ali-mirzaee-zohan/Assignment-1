a=float(input("Please enter the size of the first side : "))
b=float(input("Please enter the size of the second side : "))
c=float(input("Please enter the size of the third side : "))
if a<b+c and b<a+c and c<a+b :
    result="The shape can be drawn"
else :
    result="!! Error.The shape cannot be drawn !!"
print(result)