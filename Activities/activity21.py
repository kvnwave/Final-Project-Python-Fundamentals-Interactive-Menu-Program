isContinue = True 
def activity1():
    print("Hello World")

def activity2():
    num1 = eval(input("Please enter a number: "))
    num2 = eval(input("Please enter another number: "))
    print(f"{num1} Floor divided to {num2} = {num1 // num2}")

def activity3():
    name = input("Please input your name:")
    gender = input("Please input your gender:")
    address = input("Please input your address:")
    telephone = input("Please input your telephone number:")
    cellphone = input("Please input your cellphone number:")
    birthday = input("Please input your birthday:")
    civil_status = input("Please input your civil status:")
    birth_place = input("Please input your birth place:")
    citizenship = input("Please input your citizenship:")
    height = input("Please input your height:")
    weight = input("Please input your weight:")
    religion = input("Please input your religion:")
    occupation = input("Please input your occupation:")
    language = input("Please input languages that you speak:")

    elementary = input("Please input your school in Elementary:")
    elemgrad = input("When did you graduate?:")
    high_school = input("Please input your school in High School:")
    hsgrad = input("When did you graduate?:")
    college = input("Please your school in College:")
    collegegrad = input("When did you graduate?:")
    degree = input("Please input the degree/s you achieved:")

    company = input("Please input your company name:")
    position = input("Please input your position:")
    companyfrom = input("When did you start:")
    companyto = input("When did you leave:")

    charrefname = input("Please input the name of your characther reference:")
    charcompany = input("Please input his/her company:")
    charposition = input("Please input his/her position:")
    charcontact = input("Please input his/her number:")

    print("")
    print("\t\t\t\t\t\t-----BIODATA-----")
    print(" ")
    print("PERSONAL INFORMATION")
    print("")
    print("Name: "+name)
    print("Gender: "+gender)
    print("Address: "+address)
    print("Telephone number: "+telephone)
    print("Cellphone: "+cellphone)
    print("Birthday: "+birthday)
    print("Civil Status: "+civil_status)
    print("Place of Birth: "+birth_place)
    print("Citizenship: "+citizenship)
    print("Height: "+height)
    print("Weight: "+weight)
    print("Religion: "+religion)
    print("Occupation: "+occupation)
    print("Languages or dialect spoken or written: " +language)

    print("")
    print("EDUCATIONAL BACKGROUND")
    print("")
    print("Elementary: "+elementary)
    print("Year graduated: "+elemgrad)
    print("")
    print("High School: "+high_school)
    print("Year graduated: "+hsgrad)
    print("")
    print("College: "+college)
    print("Year graduated: "+collegegrad)
    print("Degree achieved: "+degree)

    print("")
    print("EMPLOYMENT RECORD")
    print("")
    print("Company: "+company)
    print("Position: "+position)
    print("From: "+companyfrom)
    print("To: "+companyto)

    print("")
    print("CHARACTHER REFERENCE")
    print("")
    print("Name: "+charrefname)
    print("Company: "+charcompany)
    print("Position: "+charposition)
    print("Number: "+charcontact)

def activity4():
    number1 = eval(input("Please input a number-->"))
    number2 = eval(input("Please input a number-->"))

    answer = number1 + number2

    print("The sum of" ,number1, "+" ,number2, "is",answer)

def activity5():
    pass


def activity6():
    x = 5

    print("")

    print(x)

    x += 5

    print(x)

    x += 10

    print(x)

    x += 15

    print(x)

    x += 20

    print(x)

    x += 25

    print(x)

    x += 30

    print(x)

    x += 35

    print(x)

    x += 40

    print(x)

    x += 45

    print(x)

    x += 50

    print(x)

    x += 55

    print(x)

def activity7():
    gold =  0
    miner = input("Please input your name: ")

    isGold = input("Is the mineral gold? ") 

    if isGold.lower() == "yes":
        gold +=1
        print(f"Hi! {miner}, Your total number of gold is {gold}")
    else:
        print(f"Hi! {miner}, Your total number of gold is {gold}")

def activity8():
    password = input("Please input your password--->")

    if password.lower() == "iloveyou123":
        print("Access Granted, Please continue using the system.")
        print("	-----System exit-----")
    elif password.lower() == "Hello2024!":
        print("Access Granted, Please continue using the system.")
        print("	-----System exit-----")
    elif password.lower() == "dll":
        print("Access Granted, Please continue using the system.")
        print("	-----System exit-----")
    elif password.lower() == "password":
        print("Access Granted, Please continue using the system.")
        print("	-----System exit-----")

    else:
        print("Wrong password, Please try again.")
        print("	-----System exit-----")

def activity9():
    # act 9
    # age category

    age = eval(input("Please input your age: "))

    if age <= 7:
        print("=======")
        print("Toddler")

    if age >=8 and age <=13:
        print("=======")
        print("Pre teen")

    if age >=14 and age <=18:
        print("=======")
        print("Teenager")

    if age >=19 and age <=31:
        print("=======")
        print("Early adulthood")

    if age >=32 and age <=45:
        print("=======")
        print("Mid adulthood")

    if age >=46 and age <=59:
        print("=======")
        print("Post adulthood")

    if age >=60:
        print("=======")
        print("Senior")

def activity10():
    name = input("Please input your name: ")
    isStudent = input("Are your currently enrolled in DLL?: (yes / no): ")

    if isStudent.lower() == "yes":
        yearlevel = input("What year level are you in?\n\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\n\nPlease input your answer: ")

        if yearlevel.lower() == "f":
            print(f"\nHi, {name}, Freshmen, Welcome to DLL")

        if yearlevel.lower() == "s":
            print(f"\nHi, {name}, Sophomore, Welcome back to DLL")

        if yearlevel.lower() == "j":
            print(f"\nHi, {name}, Junior, Welcome back to DLL")

        if yearlevel.lower() == "r":
            print(f"\nHi, {name}, Senior, Welcome back to DLL")

    else:
        print("\nThank you for using the system, you may now close it.\n")

def activity11():
    # loop

    for lyrics in range(1,20):
        # die with a smile
        print("If the world was ending")
        print("I wanna be next to you...")
        isParty = False
        print(f"if the party is {isParty}")
        print("And our time on earth was through")
        # opm
        print("\nSaan ba to patungo...")

def activity12():
    for x in range(10, 0, -1):
        print(x)

def activity13():
    num = eval(input(f"Enter a number: "))
    factorial = 1

    for x in range(num, 0, -1):
        factorial *= x
    print(f"The factorial of {num} is {factorial}")

def activity14():
    for x in range(0,99):
        print("*", end = " = ")

def activity15():
    for x in range(0, 11,):
        print(x, end =" ")
        for y in range(0,x):
            print("*", end =" ")
        print()

def activity16():
    for x in range(1,10):
        for y in range(1,x+1):
            print(" ", end=" ")
        for z in range(1,x,-1):
            print("*", end=" ")
        print()

def activity17():
    column = eval(input("Enter number of columns: "))
    for x in range(1,11):
        for y in range(1, column+1):
            print(f"{x} x {y} = {x * y}", end="\t")
        print()

def activity18():
    nt = eval(input("Enter number of triangles: "))
    for x in range(1,5):
        for r in range(1, nt+1):
            for y in range(1, x+1):
                print("*", end=" ")
            for z in range(5, x, -1):
                print(" ", end=" ")
            print(end=" ")
        print()

def activity19():
    isContinue = True 

    while isContinue == True:
        name = input("Give me a name ---> ")

        if name.lower() == "stop":
            print("Loop Terminated")
            break
            isContinue == False 
        else:
            print(f"Hi, {name}")
        continue

def activity20():
    isContinue = True 

    nt = 0
    while isContinue == True:
        ask = input("Gusto mo bang gumawa ng isa pang triangle (oo/hindi)")

        if ask.lower() == "hindi":
            print("Program terminated")
            break
            isContinue == False 
        
        else:
            nt += 1
            for a in range(1,6):
                for d in range(1,nt+1):
                    for b in range(1,a+1):
                        print("*",end=" ")
                    for c in range(6,a,-1):
                        print(" ",end=" ")
                    print(end=" ")
                print()
            continue    

def cc1(): 
    pass

def cc2(): 
    pass

def cc3(): 
    pass

def cc4(): 
    number1 = eval(input("Please input the first number -->"))
    number2 = eval(input("Please input the second number -->"))

    sum = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    qoutient = number1 / number2
    exponent = number1 ** number2
    remainder = number1 % number2
    floor_division = number1 // number2


    print("")
    print("Result:")
    print("")
    print("The sum of",number1,"+",number2,"is = ",sum)
    print("")
    print("The difference of",number1,"and",number2,"is = ",difference)
    print("")
    print("The product of",number1,"and",number2,"is = ",product)
    print("")
    print("The qoutient of",number1,"and",number2,"is = ",qoutient)
    print("")
    print(number1,"exponent by",number2,"is = ",exponent)
    print("")
    print("The remainder of",number1,"and",number2,"is = ",remainder)
    print("")
    print("The floor division of",number1,"and",number2,"is = ",floor_division)

def cc5(): 
    print("")
    print("FARENHEIT TO CELCIUS CONVERTER")
    print("==============================")

    farenheit = eval(input("Please input the temperature in farenheit-->"))
    celcius = ((farenheit - 32) * 5 ) / 9 #formula

    print(f"{farenheit} degrees farenheit converted to celcius is {round(celcius,2)} degrees") 

def cc6():     
    print("\nFINAL GRADE COMPUTATION")

    name = input("STUDENT'S FULL NAME: ")

    prelim = eval(input("\nPlease input your prelim grade-->"))
    midterm = eval(input("Please input your midterm grade-->"))
    semifinal = eval(input("Please input your semifinal grade-->"))
    final = eval(input("Please input your final grade-->"))
    quiz = eval(input("Please input your quiz grade-->"))
    project = eval(input("Please input your project grade-->"))

    if (prelim >= 65 and prelim <=100) + (midterm >= 65 and midterm <=100) + (semifinal >= 65 and semifinal <=100) + (final >= 65 and final <+100) + (quiz >= 65 and quiz <=100) + (project >= 65 and project <=100):
        final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
        if final_grade >= 75:  
            print(f"\n{name}, your final grade is {round(final_grade,2)}")
            print("Congratulations!, you passed!")
            print("----SYSTEM EXIT----")
        else:
            print(f"\n{name}, your final grade is {round(final_grade,2)}")
            print("Sorry, you failed.")
            print("----SYSTEM EXIT----")
    else:
        print("INVALID GRADE - Please try again")

def cc7(): 
    #grocery


    print("\nGROCERIES APP")
    name = input("\nPLease input your name: ")
    isGrocery = input("Did you buy a grocery? (yes / no): ")
    if isGrocery.lower() == "yes":
        itemname = input("Please input the item name: ")
        price = int(input("Please input the price of the item: "))
        amount = int(input("Please input your money: "))
        age = eval(input("Please input your age: "))
        if age <=59:
                tax = price * 0.123                    
                total = tax + price
                change = total - amount                          
                print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 12.3% tax ({tax}) total of {total}\nAmount given: {amount}\nChange:{round(change,2)}")
        else:
                taxs = price * 0.052
                totals = price + taxs
                changes = totals - amount
                print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 5.2% tax with senior citizen discount ({taxs}) total of {totals}\nAmount given: {amount}\nChange:{round(changes,2)}")    
    else:
        print("Thank you, you may now close this app.")

def cc8(): 
    sum = 0
    for x in range(1,11):
        num = eval(input(f"Enter number {x}: "))
        sum += num
        
    print(f"The summation of all numbers are {sum}")

def cc9(): 
    for x in range(0,11):
        if x == 1:
                print(" ", end=" ")
        elif x == 2:
                print("   ",end=" ")
        elif x == 3:
                print("     ",end=" ") 
        elif x == 4:
                print("       ",end=" ")
        elif x == 5:
                print("         ",end=" ")  
        elif x == 6:
                print("           ",end=" ")   
        elif x == 7:
                print("             ",end=" ") 
        elif x == 8:
                print("               ",end=" ")    
        elif x == 9:
                print("                 ",end=" ")          
        else:
                print()

        for y in range(10,x,-1):
                print("*", end=" ")
        print()

def cc10(): 
    for x in range(6,1,-1):
        for y in range(x,0,-1):
                print(" ", end=" ")
        for z in range(6,x,-1):
                print("*", end=" ")
        for a in range(6,x,-1):
                print("*", end=" ")
        print()

    for x in range(1,6):
        for y in range(1,x+1):
                print(" ", end=" ")
        for z in range(6,x,-1):
                print("*", end=" ")
        for a in range(6,x,-1):
                print("*", end=" ")
        print()

def cc11(): 
    for x in range(7,1,-1):
        for y in range(x,0,-1):
                print(" ", end=" ")
        for z in range(6,x,-1):
                print("*", end=" ")
        for a in range(7,x,-1):
                print("*", end=" ")
        print()

    for x in range(1,7):
        for y in range(1,x+1):
                print(" ", end=" ")
        for z in range(6,x,-1):
                print("*", end=" ")
        for a in range(7,x,-1):
                print("*", end=" ")
        print()

def cc12(): 
    for x in range(10, 0, -1):
        print(x)

def cc13(): 
    for x in range(1,6):
        for y in range(6,x,-1):
                print(" ", end=" ")
        for z in range(x,1,-1):
                print(z,end=" ")
        for a in range(1,x+1):
                print(a,end=" ")
        print()

    for x in range(4,0,-1):
        for y in range(5+1,x,-1):
                print(" ", end=" ")
        for z in range(x,1,-1):
                print(z,end=" ")
        for a in range(1,x+1):
                print(a,end=" ")
        print()

def cc14(): 
    # continue to ask user for a number
    # summation at the end of loop

    con = True
    sum = 0

    while con == True:
        num = eval(input("Please enter a number --> (put 0 to stop) "))

        if num > 0:
            sum += num
            continue

        else:
            print("\nLoop has stopped")
            print(f"The summation of all the numbers you entered is {sum}")
            break
            con = False

def cc15(): 
    import os

    tuloy = True
    no = 0
    while tuloy:
        ask = input("Do you wish to create a new triangle (yes/no) ")

        if ask.lower() == "no":
            print("program / loop terminated")
            break
        elif ask.lower() == "yes":
            os.system("cls")
            no += 1
            for x in range(1,6):
                for r in range(1, no+1):
                    for y in range(1,x+1):
                        print("^",end =" ")
                    for z in range(6,x,-1):
                        print(" ",end=" ")
                print()
            continue

        else:
            os.system("cls")
            print("Invalid answer, please only answer 'yes' or ' no' ")
            continue

def cc16():
    import os

    balance = 0
    access = False
    transaction = True

    def denomination():
        one_th = balance // 1000
        one_th_change = balance % 1000
        print(f"1000 \t=\t {one_th}")
        fiveh = one_th_change // 500
        fiveh_change = one_th_change % 500  
        print(f"500 \t=\t {fiveh}")
        twoh = fiveh_change // 200
        twoh_change = fiveh_change % 200
        print(f"200 \t=\t {twoh}")
        oneh = twoh_change // 100
        oneh_change = twoh_change % 100
        print(f"100 \t=\t {oneh}")
        fifty = oneh_change // 50
        fify_change = oneh_change % 50
        print(f"50 \t=\t {fifty}")
        twenty = fify_change// 20
        twenty_change = fify_change % 20
        print(f"20 \t=\t {twenty}")
        ten = twenty_change // 10
        ten_change = twenty_change % 10
        print(f"10 \t=\t {ten}")
        five = ten_change // 5
        five_change = ten_change % 5
        print(f"5 \t=\t {five}")
        one = five_change // 1
        one_change = five_change % 1
        print(f"1 \t=\t {one}")

    def balance_inquiry():
        print(f"\nYour balance across all account is ₱{balance}")
        print("Here is the denomination: \n")
        denomination()

    def deposit():
        amount = eval(input("Enter an amount to be deposited: "))
        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            print(f"You have successfully deposited an amount worth ₱{amount}, to see total balance and denomination, check balance inquiry.")
            return amount


    def withdraw():
        amount = eval(input("Enter amount to be withdrawn: "))
        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0")
            return 0
        else:
            print(f"You have successfully withdrawn an amount worth ₱{amount}, to see total balance and denomination, check balance inquiry.")
            return amount

    def account():
        create = input("Welcome to Bank A, Would you like to create an account? (yes / no) ")
        if create.lower() == "yes":
            bank_name = input("Enter your name: ")
            print(f"Good to see you here {bank_name}!, You may now access the bank features")
        else: 
            print("Thank you for visiting!")
            access = False

    def open_account():
        another = input("Would you like to open another account? (yes / no) ")
        if another == "yes":
            name = input("Please enter the name of your account: ")
            print(f"Good to see you here {name}!, You may now access the bank features")
        else:
            return
        
    while transaction:
        print("\n===== Welcome to Bank A! =====\n")

        print("0.Create Account")
        print("1.Open another account")
        print("2.Show Balance")
        print("3.Deposit")
        print("4.Withdraw")
        print("5.Exit")
        print("\n===============================\n")
        choice = input("Enter your choice (0-5): ")

        if choice =="0":
            os.system('cls')
            account()
            access = True
        elif choice == "1":
            if access == False:
                os.system('cls')
                print("Please create an account first")
            else:
                os.system('cls')
                open_account()
        elif choice == '2':
            if access == False:
                os.system('cls')
                print("\nPlease create an account first")
            else:
                os.system('cls')
                print("You are accessing the balance inquiry feature.")
                balance_inquiry()
        elif choice == '3':
            if access == False:
                os.system('cls')
                print("\nPlease create an account first")
            else:
                os.system('cls')
                print("You are accessing the deposit feature.")
                balance += deposit()
        elif choice == '4':
            if access == False:
                os.system('cls')
                print("\nPlease create an account first")
            else:
                os.system('cls')
                print("You are accessing the withdraw feature.")
                balance -= withdraw()
                
        elif choice == '5':
            transaction = False
        else:
            os.system('cls')
            print("\nThat is not a valid choice")

    print("\nThank you! Have a nice day!")

while isContinue:
    print("\nSelect from the following code")
    print("Activities: ")
    print("1 - Hello world")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    print("8")
    print("9")
    print("10")
    print("11")
    print("12")
    print("13")
    print("14")
    print("15")
    print("16")
    print("17")
    print("18")
    print("19")
    print("20")
    print("\nCODE CHALLENGES\nUse cc for selecting (ex: cc1)")
    print("Code Challenge 1")
    print("Code Challenge 2")
    print("Code Challenge 3")
    print("Code Challenge 4")
    print("Code Challenge 5")
    print("Code Challenge 6")
    print("Code Challenge 7")
    print("Code Challenge 8")
    print("Code Challenge 9")
    print("Code Challenge 10")
    print("Code Challenge 11")
    print("Code Challenge 12")
    print("Code Challenge 13")
    print("Code Challenge 14")
    print("Code Challenge 15")
    print("Code Challenge 16")

    print("100 - EXIT")
    ask = input("\nWhich program would you like to run, select options from above: ")

    if ask == "1":
        print("ACTIVITY 1\n")
        activity1()
        continue

    if ask == "2":
        print("ACTIVITY 2\n")
        activity2()
        continue

    if ask == "3":
        print("ACTIVITY 3\n")
        activity3()
        continue
    
    if ask == "4":
        print("ACTIVITY 4\n")
        activity4()
        continue

    if ask == "5":
        print("ACTIVITY 5\n")
        activity5()
        continue

    if ask == "6":
        print("ACTIVITY 6\n")
        activity6()
        continue

    if ask == "7":
        print("ACTIVITY 7\n")
        activity7()
        continue

    if ask == "8":
        print("ACTIVITY 8\n")
        activity8()
        continue

    if ask == "9":
        print("ACTIVITY 9\n")
        activity9()
        continue
    
    if ask == "10":
        print("ACTIVITY 10\n")
        activity10()
        continue
    
    if ask == "11":
        print("ACTIVITY 11\n")
        activity11()
        continue

    if ask == "12":
        print("ACTIVITY 12\n")
        activity12()
        continue

    if ask == "13":
        print("ACTIVITY 13\n")
        activity13()
        continue
    
    if ask == "14":
        print("ACTIVITY 14\n")
        activity14()
        continue
    
    if ask == "15":
        print("ACTIVITY 15\n")
        activity15()
        continue
    
    if ask == "16":
        print("ACTIVITY 16\n")
        activity16()
        continue
    
    if ask == "17":
        print("ACTIVITY 17\n")
        activity17()
        continue
    
    if ask == "18":
        print("ACTIVITY 18\n")
        activity18()
        continue
    
    if ask == "19":
        print("ACTIVITY 19\n")
        activity19()
        continue
    
    if ask == "20":
        print("ACTIVITY 20\n")
        activity20()
        continue

    if ask == "cc1":
        print("Code Challenge 1")
        cc1()
        continue

    if ask == "cc2":
        print("Code Challenge 2")
        cc2()
        continue

    if ask == "cc3":
        print("Code Challenge 3")
        cc3()
        continue

    if ask == "cc4":
        print("Code Challenge 4")
        cc4()
        continue

    if ask == "cc5":
        print("Code Challenge 5")
        cc5()
        continue

    if ask == "cc6":
        print("Code Challenge 6")
        cc6()
        continue

    if ask == "cc7":
        print("Code Challenge 7")
        continue

    if ask == "cc8":
        print("Code Challenge 8 ")
        cc8()
        continue

    if ask == "cc9":
        print("Code Challenge 9")
        cc9()
        continue

    if ask == "cc10":
        print("Code Challenge 10")
        cc10()
        continue

    if ask == "cc11":
        print("Code Challenge 11")
        cc11()
        continue

    if ask == "cc12":
        print("Code Challenge 12")
        cc12()
        continue
    
    if ask == "cc13":
        print("Code Challenge 13")
        cc13()
        continue

    if ask == "cc14":
        print("Code Challenge 14")
        cc14()
        continue

    if ask == "cc15":
        print("Code Challenge 15")
        cc15()
        continue

    if ask == "cc16":
        print("Code Challenge 16")
        cc16()
        continue

    if ask.lower() == "100":
        print("Program terminated")
        break

    else:
        print("Invalid Choice, Please try again. ")
        continue