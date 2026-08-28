i=5
if(i<2):
    print("Inside if statement")
print("Outside if statement")

ch=input("Enter a single charecter :")
if(ch>='0' and ch<='9'):
    print('you entered a digit.')



x=5
y=10
if(x>y):
    print("x is greater= ",x)
else:
    print("Y is greater= ",y)
print("Outside if and else block block")





a=int(input("Enter any number :"))
if(a>=0):
    print(a," is zero or a positive number")
else:
    print(a," is a negative number")



    
    
num=int(input("Enter any number :"))
if(num%2==0): 
    print(num," is EVEN number")
else:
    print(num," is ODD number")



x=y=x=0
x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
z=float(input("Enter third number: "))
max=x               
if(y>max):
     max=y
if(z>max):
     max=z
print("largest number is ",max)





salary=input("Enter your salary: ")
salary=int(salary)
age=input("Enter your age: ")
age=int(age)
bonus=0
if(age > 50):
    if(salary > 10000):
         bonus=2000
    else:
         bonus=1000
    netsalary=salary+bonus
    print("Bonus: ",bonus)
    print("Net salary: ",netsalary)
else:
    print("You are not eligible for bonus")




run=int(input("Enter run: "))
if(run>=100):
    print("Batsman scored a century")
elif(run>=50):
    print("Batsman scored a fifty")
else:
    print("Batsman has neither scored a century nor fifty")




num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
op=input("Enter operator[+ - * / %]:")
result=0
if(op=='+'):
    result=num1+num2
elif(op=='-'):
    result=num1-num2
elif(op=='*'):
    result=num1*num2
elif(op=='/'):
    result=num1/num2
elif(op=='%'):
    result=num1%num2
else:
    print("Invalid operator!!!")
print(num1,op,num2,'=',result)




marks=input("Enter marks obtain: ")
marks=int(marks)
if(marks>=90):
    print("Grade A+")
elif(marks>=75):
    print("Grade A")
elif(marks>=60):
    print("Grade B")
elif(marks>=45):
    print("Grade C")
elif(marks>=30):
    print("Grade D")
else:
    print("FAIL")




x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
z=float(input("Enter third number: "))
print("max number ")             
if(x>y and x>z):
     print(x)
elif(y>x and y>z):
    print(y)
else:
    print(z)
    


