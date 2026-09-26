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
else:
    if rating==5:
        if experience>=5:
            bonus_amount = basic_salary * (20/ 100)
            final_salary = basic_salary + bonus_amount
            print("bonus_amount : ",bonus_amount)
            print("final salary :",final_salary)
            print("bonus percentage : ", 20,"%" )
       else:
