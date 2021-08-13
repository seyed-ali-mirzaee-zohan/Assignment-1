first_name=input(" Please enter your firstname : ")
last_name=input(" Please enter your lastname : ")
first_lesson=float(input(" Please enter the grade of the first lesson : "))
second_lesson=float(input(" Please enter the grade of the second lesson : "))
third_lesson=float(input(" Please enter the grade for the third lesson : "))
average=(first_lesson+second_lesson+third_lesson)/3
if average<12:
    result=" fail "
if 12<=average<17:
    result=" noraml " 
if average>=17 :
    result= " graet "
print(result)