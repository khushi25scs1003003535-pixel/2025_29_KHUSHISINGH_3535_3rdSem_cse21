# you are required to build a simple finance managrement tool.

expense = [] #list of expense in form of dictonary
print("welcome to expense tracker ")
while True:
    print("----menu----")
    print("1.add expenses")
    print("2.view all expenses")
    print("3.view total expenses")
    print(" 4.exit")

    choice  = int(input("please enter your choice"))

    if(choice == 1):
        date = input("enter your date")
        category = input("enter category")
        description = input("deatils about product")
        amount =float( input("enter the amount"))

        new_expense = {
            "date": date,
            "category" : category,
            "description" : description,
            "amount": amount


        }

        expense.append(new_expense)
        print(" \n expense is added successfully")
    if(choice == 2):
        if(len(expense)==0):
            print("no expense is added ")   
        else :
            print("all your expense")
            count = 1
            for eachexpense in expense:
                  print(f"Expense number{count}->" f"{eachexpense["date"]},"f"{eachexpense["category"]},"f"{eachexpense["description"]},"f"{eachexpense["amount"]}")

                  count  = count + 1

    elif(choice == 3):
       total = 0
       for eachexpense in expense:
            total =  total + eachexpense["amount"]
       print("\n total expense = ", total)

    elif(choice == 4):
           print("thankyou for using my system") 
           break
    else:
     print("invalid choice , please try again")       

                

 

