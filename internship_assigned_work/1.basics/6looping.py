for a in [1, 4, 7]:
    print(a)
    print(a*a)




for val in range(1,10):
     print(val)



print("Range with one parameter:")
for val1 in range(5):
    print(val1)
print("Range with two parameter:")
for val2 in range(1,5):
    print(val2)
print("Range with three parameter:")
for val3 in range(1,10,3):
    print(val3)




num=int(input("Enter a number: "))
for a in range(1,11):
    print(num,'x',a,'=',num*a)


sum=0
for n in range(1,8):
    sum+=n
    print("sum of natural numbers <=",n,"is",sum)


sum=0
for n in range(1,8):
    sum+=n
print("sum of natural numbers <=",n,"is",sum)


a=5
while a>0:
    print("Hello",a)
    a=a-1



    a=1
while (a<=10):
     print(a)
     a=a+1



a=2
while (a<=10):
    print(a)
    a=a+2



num=1
while (num<=5):
    print('Square of',num,'is',num*num)
    num+=1
print("Thank you !!!")




num=int(input("Enter a number: "))
fact=1
n=num
while(num>=1):
    fact=fact*num;
    num-=1
print("Factorial of", n ,"=",fact)




num=int(input("Enter a number: "))
i=1
while (i<=10):
    print(num,"x",i,"=",num*i)
    i+=1
