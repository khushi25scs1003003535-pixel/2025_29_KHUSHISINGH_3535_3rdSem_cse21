for val in [1,2,3,4,5]:
    if val == 4:
        break
    print(val)
print("The end")



for val in "Internshipwala":
    if val == "w":
        break
    print(val)
print("Thank you !!!")




for val in [1,2,3,4,5]:
    if val == 4:
        continue
    print(val)
print("Thank You")





for val in "Internshipwala":
    if val == "w":
        continue
    print(val)
print("Thank you !!!")





a=2
while True:
     print(a)
     a*=2
     if(a>100):
         break





num=1
print("Odd number between 1 to 10:")
while(num<=10):
    if (num %2==0):
        num+=1
        continue
    print(num)
    num=num+1
print("Thank You")




for i in range(1, 4):
     print(i)
else:
    print("No Break")




for i in range(1, 4):
     print(i)
     break
else:
    print("No Break")




count = 0
while (count > 1):
     count = count+1
     print(count)
     break
else:
    print("Else block")





count = 0
while (count < 1):
     count = count+1
     print(count)
     break
else:
    print("Else block")
