#Employee salary and Bonus checker......
name=input("enter employee name : ")
basic_salary=int(input("enter basic salary : "))
experience=int(input("enter year of experience : "))
rating=int(input("enter performance rating 1 to 5 : "))
print("Employee name : ", name)
print("Basic salary : ", basic_salary)
if basic_salary<0 :
    print("Invalid salary ")                            
elif experience<0 :
    print("Invalid experience ")
elif rating<1 or rating>5 :
    print("Invalid rating")   
