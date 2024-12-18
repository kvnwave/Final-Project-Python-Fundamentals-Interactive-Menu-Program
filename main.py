import sys
#explanations for each code starts here
def act1_help(): 
      print("""\n \033[1m
      This code uses 'print' to create a diamond shape
      code:
      print("\ t\ t       * \ n\ t\ t     *  
       *\ n\ t\ t   *   *   *\ n \ t       *   *
         *   *   *\ n\ t\ t   *   *   *\ n\ t\ t     
         *   *\ n\ t\ t       * ")
      
      breakdown:
      \ n and \ t are excape sequences.
      \ n is used to create a new line without using another 'print'
      \ t is for tab space
      
      note: escape sequences work with this format '\ n'(no space between \ and n )
      You can use space as tab space created by \ t isn't easy to align.\033[0m""")

def activity3_help():
      print("""\n \033[1m
      This program uses 'variable' to create question and will then be compiled later
      code:
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
      print("\ t\ t\ t\ t\ t\ t-----BIODATA-----")
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

      You can create a variable using this format:
            variable = action to run
            You can use 'input' which asks the user a question 
            that will be stored and display upon calling. \033[0m
      """)

def code_challenge2_help():
      
     print(""" 
     name = input("Enter your name: ")
     print(f"\ t\ t       * \ n\ t\ t      *   *\ n\ t\ t   *   *   *\ n\ t       *     {name}    *\ n \ t\ t   *   *   *\ n \ t \ t     *   *\ n \ t\ t        * ")
     """)

def activity4_help():
      print("""\033[1m
      This program uses 'variable' with 'operators' to execute it's task

      code:
      number1 = eval(input("Please input a number-->"))
      number2 = eval(input("Please input a number-->"))

      answer = number1 + number2

      print("The sum of" ,number1, "+" ,number2, "is",answer)
            
      breakdown:
            number1 and number2 = variables that will store the 2 numbers to be asked
            answer = variable that will add the two numbers that were gathered with the 2  \033[0m 
      """)

def code_challenge5_help():
      print("""\033[1m
      This code converts Celcius to Farentheit
      
      code:
      print("")
      print("FARENHEIT TO CELCIUS CONVERTER")
      print("==============================")

      farenheit = eval(input("Please input the temperature in farenheit-->"))
      celcius = ((farenheit - 32) * 5 ) / 9 #formula

      print(f"{farenheit} degrees farenheit converted to celcius is {round(celcius,2)} degrees") 
      
      breakdown:
            farenheit - variable to get the temperature in farenheit
            celcius - formula for converting farenheit into celcius \033[0m
      """)

def act6_help():
      print("""\033[1m
      This program will store the first number then it will be added with next number
            
      code:
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

      breakdown:
            x = 5 - first number
            x += 5 - it is the same as x = x + 5
            It will store the result and add it to the next number assigned \033[0m
      """)


def code_challenge4_help():
      print("""\033[1m
      This program will ask for 2 numbers that will be used for different operations
            
      code:
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

      breakdown:
            These two are assigned to get the number 
                  number1 = eval(input("Please input the first number -->"))
                  number2 = eval(input("Please input the second number -->"))
            It will then be used for these operations:
                  sum = number1 + number2
                  difference = number1 - number2
                  product = number1 * number2
                  qoutient = number1 / number2
                  exponent = number1 ** number2
                  remainder = number1 % number2
                  floor_division = number1 // number2 \033[0m
      """)

def act7_help():
      print(""" \033[1m
      This program adds 1 count to gold if the mineral is gold
            
      code:
      gold =  0
      miner = input("Please input your name: ")

      isGold = input("Is the mineral gold? ") 

      if isGold.lower() == "yes":
            gold +=1
            print(f"Hi! {miner}, Your total number of gold is {gold}")
      else:
            print(f"Hi! {miner}, Your total number of gold is {gold}")
      
      breakdown:
            gold = 0 - variable for storing the number of gold, 
            so the first count will be 1
            .lower() - converts all input into lowercase \033[0m
            """)
def act8_help():
      print(""" \033[1m
      This program will let the user access the sytem if the password is correct
            
      code:
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
            print("	-----System exit-----") \033[0m
            """)

def act9_help():
      print("""\033[1m
      This program will evaluate your Age based on what you will input
            
      code:
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

      breakdown:
            if - else - to sort the data that will be sent
            if the condition is met, it will print the text within that condition
      \033[0m""")

def act10_help():
      print("""\033[1m
      This program evaluates your Student Status
            
      code:
            name = input("Please input your name: ")
            isStudent = input("Are your currently enrolled in DLL?: (yes / no): ")

            if isStudent.lower() == "yes":
                  yearlevel = input("What year level are you in?\ n\ nF - Freshmen\ nS -
                  Sophomore\ nJ - Junior\ nR - Senior\ n\ nPlease input your answer: ")

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
      \033[0m""")

def code_challenge6_help():
      print("""\033[1m
      This program computes your final grade
      
      code:            
      print("\nFINAL GRADE COMPUTATION")

      name = input("STUDENT'S FULL NAME: ")

      prelim = eval(input("\nPlease input your prelim grade-->"))
      midterm = eval(input("Please input your midterm grade-->"))
      semifinal = eval(input("Please input your semifinal grade-->"))
      final = eval(input("Please input your final grade-->"))
      quiz = eval(input("Please input your quiz grade-->"))
      project = eval(input("Please input your project grade-->"))

      if (prelim >= 65 and prelim <=100) + (midterm >= 65 and midterm <=100) + (
      semifinal >= 65 and semifinal <=100) + (final >= 65 and final <+100) + 
      (quiz >= 65 and quiz <=100) + (project >= 65 and project <=100):

      final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) +
      (quiz * 0.25) + (project * 0.15)
            
      if final_grade >= 75:  
            print(f"\n{name}, your final grade is {round(final_grade,2)}")
            print("Congratulations!, you passed!")
            print("----SYSTEM EXIT----")
      else:
            print(f"\n{name}, your final grade is {round(final_grade,2)}")
            prinint("----SYSTEM EXIT----")
      else:
      print("INVALID GRADE - Please try again")
                  
      \033[0m""")

def code_challenge7_help():
      print("""\033[1m
      This program helps you with your grocery

      code:
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
                  change = amount - total           
                  print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 12.3% tax ({tax}) total of ({total})\nAmount given: {amount}\nChange:{round(change,2)}")
            else:
                  taxs = price * 0.123
                  totals = price + taxs
                  discount = totals * 0.052
                  overall = totals - discount
                  changes = amount - overall
                  print(f"\nHi {name}, you purchased {itemname}, with a price of {price} plus 12.3% tax ({taxs}) total of ({totals}) with senior citizen discount of 5.2% ({discount}) with the overall total ({overall})\nAmount given: {amount}\nChange:{round(changes,2)}")    
      else:
            print("Thank you, you may now close this app.")

      
      \033[0m""")

def activity11_help():
      print("""\033[1m
      This program will loop a certain code for a given amount of iteration
      
      code:
            # loop

            for lyrics in range(1,20):
            # die with a smile
            print("If the world was ending")
            print("I wanna be next to you...")
            isParty = False
            print(f"if the party is {isParty}")
            print("And our time on earth was through")
            # opm
            print("Saan ba to patungo...")

      breakdown:
            lyrics - name 
            range - in charge for the number of iteratios
            range(1,20) - 1 is the starting point while 20 is the end point,
            but take note that 20 will not be counted, it will stop at 19
      \033[0m""")

def activity12_help():
      print("""\033[1m
      This program counts from 1 to 10
      
      code:
            for x in range(10, 0, -1):
            print(x)

      breakdown:
            print(x) - x is will iterated
            for x in range(10,0,-1) - x is the placeholder, 10 is the starting
            point, 0 is the end point (it will stop at 1), while - 1 is the step
            which means it will count backwards
      \033[0m""")

def activity13_help():
      print("""\033[1m
      This program solves the factorial of a number for you
      
      code:
      
      num = eval(input(f"Enter a number: "))
      factorial = 1

      for x in range(num, 0, -1):
      factorial *= x
      print(f"The factorial of {num} is {factorial}")
      
      breakdown:
            num - variable to get the number
            factorial = 1 - initial value for factorial
            factorial *= x - factorial will be multiplied
            to the value of x and will be stored for 
            the next operation

      \033[0m""")  

def activity14_help():
      print("""\033[1m
      This program will count to 10 with a line of *
            
      code:
      for x in range(0,11):
            print(x, end =" ")
            for y in range(0,11):
                  print("*", end =" ")
            print()
      \033[0m""")

def activity15_help():
      print("""\033[1m
      This program runs an acute triangle
      
      code:

      for x in range(0, 11,):
            print(x, end =" ")
            for y in range(0,x):
                  print("*", end =" ")
            print()
      \033[0m""")

def activity17_help():
      print("""\033[1m
      This program creates a multiplication table based on 
      the number of columns
      
      code:
      column = eval(input("Enter number of columns: "))
      for x in range(1,11):
      for y in range(1, column+1):
            print(f"{x} x {y} = {x * y}", end="\t")
      print()
      
      \033[0m""")

def activity18_help():
      print("""\033[1m
      This program generates a number of triangle
      based on the amount given
      
      code:
      nt = eval(input("Enter number of triangles: "))
      for x in range(1,5):
      for r in range(1, nt+1):
            for y in range(1, x+1):
                  print("*", end=" ")
            for z in range(5, x, -1):
                  print(" ", end=" ")
            print(end=" ")
      print()
      \033[0m""")

def code_challenge8_help():
      print("""\033[1m
      This program asks for 10 numbers and will
      display the summation of all numbers
            
      code:
      sum = 0
      for x in range(1,11):
            num = eval(input(f"Enter number {x}: "))
            sum += num
            
      print(f"The summation of all numbers are {sum}")
      \033[0m""")

def code_challenge9_help():
      print("""\033[1m
      This program inversed version of acute triangle
      
      code:
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
      \033[0m""")

def code_challenge10_help():
      print("""\033[1m
      This program generates a diamond
      
      code:
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
      \033[0m""")

def code_challenge11_help():
      print("""\033[1m
      This program generates a perfect shape diamond
      code:
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
      \033[0m""")

def code_challenge12_help():
      print("""\033[1m
      This program creates an arrow sign
            
      code: 
      for x in range(6,1,-1):
      for y in range(x,0,-1):
            print(" ",end=" ")
      for z in range(6,x,-1):
            print("*",end=" ")
      for a in range(6,x,-1):
            print("*",end=" ")
      print()

      for x in range(5,0,-1):
      print(" ",end=" ")
      for y in range(4,0,-1):
            print(" ",end=" ")
      for z in range(2,0,-1):
            print("*",end=" ")
      print()
      \033[0m""")

def code_challenge13_help():
      print("""\033[1m
      This program creates diamond but using nummbers
      
      code:
      for x in range(1,6):
      for y in range(6,x,-1):
            print(" ", end=" ")
      for z in range(x,1,-1):
            print(z,end=" ")
      for a in range(1,x+1):
            print(a,end=" ")
      print()

      or x in range(4,0,-1):
      for y in range(5+1,x,-1):
            print(" ", end=" ")
      for z in range(x,1,-1):
            print(z,end=" ")
      for a in range(1,x+1):
            print(a,end=" ")
      print()
      \033[0m""")

def activity19_help():
      print("""\033[1m
      This program will continue to ask for name until the user 
            ends the program
      
      code:
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
      \033[0m""")

def activity20_help():
      print("""\033[1m
      Thisi program creates a triangle until
            the  user ends it

      code:
      isContinue = True 

      nt = 0
      while isContinue == True:
      ask = input("Gusto mo bang gumawa ng isa pang triangle (oo/hindi)")

      if ask.lower() == "stop":
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
            
      breakdown:
            isContinue = True - variable in-charge for the
            start and end of the loop
            The loop will end if this variable
            becomes False
      \033[0m""")

def code_challenge14_help():
      print("""\033[1m
      This program will ask for a number and 
            will only stop if the user inputs 0

      code:
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

      \033[0m""")

def code_challenge15_help():
      print("""\033[1m
      This program creates triangle until the user
            stops it

      code:
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
            
      breakdown:
            import os - type of module
      \033[0m""")

def activity25_help():
      print("""\033[1m
      This program creates a list of fruits
      
      code:
      # list

      # fruit1 = "apples"
      # fruit2 = "orange"
      # fruit3 = "starapple"
      # fruit4 = "bayabas"
      # fruit5 = "durian"
      #            0           1           2           3           4
      fruits = ["apples","oranges","star-apple","guyabano","sour soup"]
                  # data inside a list is called 'item'
      print(fruits)

      #acccess indivually the item
      print(f"My favorite fruit growing up is {fruits[2]}")
      fruits.append("Longgan")
      print(fruits)
      fruits.insert(3,"banana")
      print(fruits)     
            
      breakdown:
            fruits - a list, the count will start at 0
            fruits.append("") - will add an item at the
            end of list
            fruits.insert("") - will insert an item
            at the designated location

      \033[0m""")

def activity22_help():
      print("""\033[1m
      This program is a mini menu
            
      code:
      def panghello():
      print("HELLO IT1A")

      def activity2():
            num1 = eval(input("Please enter a number: "))
            num2 = eval(input("Please enter another number: "))
            print(num1, "Floor divided to ",num2, "=",num1 // num2)

      isContinue = True
      while isContinue:
            print("SELECT FROM THE FOLLOWING CODE \n1 = PANGHELLO 
            \n2 = DIVISION PROGRAM\n3 = EXIT")

            ask = input("Which program would you like to run, 
            select from the option above: ")

            if ask == "1":
                  panghello()
                  continue
            elif ask == "2":
                  activity2()

            elif ask == "3":
                  print("PROGRAM TERMINATED")
                  break

            else:
                  print("Invalid Choice")
                  continue
      \033[0m""")

def activity23_help():
      print("""\033[1m
      This program implements the help() code
      def factorial(number):
            This function's purpose is to compute / calculate the factorial of any number 
            fact = 1 
            for x in range(number,0,-1):
                  fact *= x
                  return fact

      print(f"The factorial of 13 is {factorial(13)}")
      help(factorial)
      help(print)
      \033[0m""")

def code_challenge16_help():
      print("""\033[1m
      This program is a mini bank program
      
      code:
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
      \033[0m""")
#explanations for each code ends here



def start():
      print("--- PYTHON PROGRAM MENU  ---") #replace nalang
      user = input("Before accessing the program, we will need to know your name\nInput it here: ")
      print(f"Hello {user}, You may now access the program")
      main_menu()

def display_menu(): #main menu
      print(f"""\033[92m 
      =======================================================
                              MENU 
         1 - print statements                              
         2 - variables                                     
         3 - operators                                     
         4 - conditional statements                        
         5 - loops                                        
         6 - lists                                         
         7 - functions                                     
         8 - exit                                  
      =======================================================   
      \033[0m""")  

def print_statements_option1():
      print()
      print("""\t
      HOW DOES PRINT WORK?
      You can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.
      Then, these parameters are represented as strings by their respective str() functions. To create a single output string, 
      the transformed strings are concatenated with spaces between them""")
      return print_statements_menu() 

def print_statements_option2(): 
      print()
      from Activities import activity1
      act1_help()
      return print_statements_menu()

def print_statements_option3():
      return main_menu()

def print_statements_menu():
      print("\nACCESSING PRINT STATEMENTS MENU")
      print("\nPython print() function prints the message to the screen or any other standard output device.")
      print("\nChoose from options below:")
      print("1. How does it works?")
      print("2. Sample program - 1")
      print("3. Return")
      print_choice = input("Enter your choice: ")
      print_choice_option(print_choice)
      return 

def print_choice_option(print_choice):
      if print_choice == "1":
            print_statements_option1()
      if print_choice == "2":
            print_statements_option2()
      if print_choice == "3":
            print_statements_option3()
      else:
            print("Invalid Choice")

def main_menu():
      isContinue = True
      while isContinue:
            display_menu()  # Show the menu options
            choice = input("Enter your choice: ")     
            if choice == '1':
                  print("You chose option 1: Print statements.")
                  print_statements_menu()
            if choice == '2':
                  print("You chose option 2: Variables.")
                  variables_menu()
            if choice == '3':
                  print("You chose option 3: Operators.")
                  operators_menu()
            if choice == '4':
                  print("You chose option 4: Conditional statements.")
                  conditionalstatements_menu()
            if choice == '5':
                  print("You chose option 5: Loops.")
                  loops_menu()
            if choice == '6':
                  print("You chose option 6: Lists.")
                  lists_menu()
            if choice == '7':
                  print("You chose option 7: Functions.")
                  function_menu()
            if choice == "8":
                  print("Program Terminated, You may now close it. ")
                  sys.exit()
            else:
                  print("Invalid choice. Please try again.")
        
        
def variables_menu():
      print("""\nACCESSING VARIBLES MENU
      Variables are containers for storing data values.
      Choose from the options below:
            
      1. How does it work?
      2. Sample Programs
      3. Return
      """)
      variable_choice = input("Enter your choice: ")
      variables_option(variable_choice)
      return 

def  variables_option(variable_choice):
      if variable_choice == "1":
            variable_choice_option1()
      if variable_choice == "2":
            variable_choice_option2()
      if variable_choice == "3":
            main_menu()

def variable_choice_option1():
      print("""HOW DOES VARIABLES WORK?
      In Python, variables are symbolic names that refer to objects or values stored in your computer’s memory. 
      They allow you to assign descriptive names to data, making it easier to manipulate and reuse values throughout your code.

      Understanding variables is key for Python developers because variables are essential building blocks for any Python program. 
      Proper use of variables allows you to write clear, readable, and maintainable code.
""")
      variables_menu()

def variable_choice_option2():
      print("You're accessing the sample programs using variable.")
      print("Choose from the option below")
      print("""
      1. Bio-data
      2. Putting a name on the center of a diamond
      3. Return
      """)
      variable_sampleprogramchoice = input("Enter your choice: ")
      variable_sampleprogram(variable_sampleprogramchoice)
      return variable_sampleprogramchoice

def variable_choice_option3():
      variables_menu()
def variable_sampleprogram(variable_sampleprogramchoice):
      if variable_sampleprogramchoice == "1":
            from Activities import activity3_aguilera
            activity3_help()
            return variable_choice_option2()
      if variable_sampleprogramchoice == "2":
            from code_challenges import code_challenge2
            code_challenge2_help()
            return variable_choice_option2()
      else:
            print("Invalid Choice")

def operators_menu():
      print("""
      ACCESSING OPERATORS MENU
      Operators are used to perform operations on variables and values.
      Choose from the options below:
      
      1. How does it work?
      2. Sample programs
      3. Return
      """)
      operators_choice = input("Enter your choice: ")
      operators_choice_options(operators_choice)
      return

def operators_choice_options(operators_choice):
      if operators_choice == "1":
            operators_choice_option1()
      elif operators_choice == "2":
            operators_choice_option2()
      elif operators_choice == "3":
            return main_menu()
      else:
            print("Invalid choice")

def operators_choice_option1():
      print("""
      Python operators are special symbols or keywords used to perform operations on variables and values. 
      These operators allow for various functionalities, from basic arithmetic operations like addition, subtraction, 
      multiplication, and division to more complex comparisons and logical operations. Python provides several types of 
      operators, including arithmetic operators for mathematical calculations, comparison operators to compare values, and 
      assignment operators to assign values to variable
      """)
      operators_menu()

def operators_choice_option2():
      print("\nYou're accessing the sample programs using operators on python")
      print("Choose from the option below")
      print("""
      1. Adding two numbers
      2. Temperature Converter
      3. Multiplication table using addition assignment operator
      4. Two numbers in all operators 
      5. Return
      """)
      operators_sampleprogramchoice = input("Enter your Choice: ")
      operators_sampleprogram(operators_sampleprogramchoice)
      return operators_sampleprogramchoice

def operators_sampleprogram(operators_sampleprogramchoice):
      if operators_sampleprogramchoice == "1":
            from Activities import activity4
            activity4_help()
            operators_choice_option2()
      elif operators_sampleprogramchoice == "2":
            from code_challenges import code_challenge5
            code_challenge5_help()
            operators_choice_option2()
      elif operators_sampleprogramchoice == "3":
            from Activities import activity6
            act6_help()
            operators_choice_option2()
      elif operators_sampleprogramchoice == "4":
            from code_challenges import code_challenge4
            code_challenge4_help()
            operators_choice_option2()
      elif operators_sampleprogramchoice == "5":
            operators_menu()
      else:
            print("Invalid Choice")

def conditionalstatements_menu():
      print("""
      Conditional Statements are statements in Python that provide a choice for the control flow based on a condition.
      
      1. How does it work?
      2. Sample programs
      3. Return
      """)
      conditionalstatements_choice = input("Enter your choice:")
      conditionalstatements_option(conditionalstatements_choice)
      return conditionalstatements_choice
      
def conditionalstatements_option(conditionalstatements_choice):
      if conditionalstatements_choice == "1":
            conditionalstatements_option1()
      elif conditionalstatements_choice == "2":
            conditionalstatements_option2()
      elif conditionalstatements_choice == "3":
            main_menu()

def conditionalstatements_option1():
      print("""
      In Python, conditional statements allow you to execute different blocks of code based on certain conditions. 
      The most common types of conditional statements are if, elif (else if), and else. 
      These statements enable decision-making in your program.
      """)
      conditionalstatements_menu()

def conditionalstatements_option2():
      print("""
      You're accessing the conditional statements sample programs
      Choose from the option below:
            
      1. Gold program
      2. Password program
      3. Stage of life program
      4. DLL student status
      5. Final Grade computation
      6. Groceries program
      7. Return
      """)
      conditionalstatements_option2_choice = input("Enter your Choice: ")
      conditionalstatements_sampleprogram(conditionalstatements_option2_choice)
      return conditionalstatements_option2_choice

def conditionalstatements_sampleprogram( conditionalstatements_option2_choice):
      if  conditionalstatements_option2_choice == "1":
            from Activities import activity7
            act7_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "2":
            from Activities import activity8
            act8_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "3":
            from Activities import activity9
            act9_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "4":
            from Activities import activity10
            act10_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "5":
            from code_challenges import code_challenge6
            code_challenge6_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "6":
            from code_challenges import code_challenge7                 
            code_challenge7_help()
            conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "7":
            conditionalstatements_menu()
      else:
            print("Invalid Choice")

def loops_menu():
      print("""
      ACCESSING MENU FOR LOOPS
      A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.
      Choose from the options below:
            
      1. How does it work?
      2. Sample programs
      3. Return
      """)
      loops_menu_choice = input("Enter your choice: ")
      loops_choice_option(loops_menu_choice)
      return

def loops_choice_option(loops_menu_choice):
      if loops_menu_choice == "1":
           loops_choice_option1()
      elif loops_menu_choice == "2":
           loops_choice_option2()
      elif loops_menu_choice == "3":
            main_menu()
      else:
            print("Invalid Choice")


def loops_choice_option1():
      print("""
      Python loops are fundamental constructs that allow you to execute a block of code repeatedly. 
      There are primarily two types of loops in Python: for loops and while loops. 
      Each serves different purposes and is used based on the specific requirements of your program.
      
      For Loops
      Definition: A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in that sequence.
            
      While Loops
      Definition: A while loop continues to execute as long as a specified condition is true.
      """)
      loops_menu()

def loops_choice_option2():
      print("""
      You're accessing sample programs using loops.
      Choose from the option below:
            
      1. For loops
      2. While loops
      3. Return
      """)
      loops_choice_option2_choice = input("Enter your choice: ")
      loops_sampleprograms(loops_choice_option2_choice)
      return loops_choice_option2_choice

def  loops_sampleprograms(loops_choice_option2_choice):
      if loops_choice_option2_choice == "1":
            for_loops()
      elif loops_choice_option2_choice == "2":
            while_loops()
      elif loops_choice_option2_choice == "3":
            loops_menu()
      else:
            print("Invalid Choice")

def for_loops(): 
      print("""
      You're accessing For loop sample programs
      Choose from the option below:
            
      1. Lyrics loop  
      2. Countdown
      3. Factorial using loop
      4. Countdown with *
      5. Right angle triangle program
      6. Multiplication table
      7. Triangle generator
      8. Input 10 numbers
      9. Inverted Triangle
      10. Diamond
      11. Diamond with tip
      12. Arrow
      13. Diamond but numbers
      14. Return
      """)
      for_loops_choice = input("Enter your choice: ")
      for_loops_menu(for_loops_choice)
      return for_loops_choice

def for_loops_menu(for_loops_choice):
      if for_loops_choice == "1":
            from Activities import activity11
            activity11_help()
            for_loops()
      elif for_loops_choice == "2":
            from Activities import activity12
            activity12_help()
            for_loops()
      elif for_loops_choice == "3":
            from Activities import activity13
            activity13_help()
            for_loops()
      elif for_loops_choice == "4":
            from Activities import activity14
            activity14_help()
            for_loops()
      elif for_loops_choice == "5":
            from Activities import activity15
            activity15_help()
            for_loops()
      elif for_loops_choice == "6":
            from Activities import activity17
            activity17_help()
            for_loops()
      elif for_loops_choice == "7":
            from Activities import activity18
            activity18_help()
            return for_loops()
      elif for_loops_choice == "8":
            from code_challenges import code_challenge8
            code_challenge8_help()
            for_loops()
      elif for_loops_choice == "9":
            from code_challenges import code_challenge9
            code_challenge9_help()
            for_loops()
      elif for_loops_choice == "10":
            from code_challenges import code_challenge10
            code_challenge10_help()
            for_loops()
      elif for_loops_choice == "11":
            from code_challenges import code_challenge11
            code_challenge11_help()
            for_loops()
      elif for_loops_choice == "12":
            from code_challenges import code_challenge12
            code_challenge12_help()
            for_loops()
      elif for_loops_choice == "13":
            from code_challenges import code_challenge13
            code_challenge13_help()
            for_loops()
      elif for_loops_choice == "14":
            loops_choice_option2()
      else:
            print("Invalid Choice")

def while_loops(): 
      print("""
      You're accessing While loop sample programs
       from the option below:
      1. Hello <name>
      2. Infinite triangle generator
      3. Input infinite number with summation at the end
      4. Infinite triangle
      5. Return
      """)
      while_loops_choice = input("Enter a number: ")
      while_loops_menu(while_loops_choice)
      return while_loops_choice

def  while_loops_menu(while_loops_choice):
      if while_loops_choice == "1":
            from Activities import activity19
            activity19_help()
            while_loops()
      elif while_loops_choice == "2":
            from Activities import activity20
            activity20_help()
            while_loops()
      elif while_loops_choice == "3":
            from code_challenges import code_challenge14
            code_challenge14_help()
            while_loops()
      elif while_loops_choice == "4":
            from code_challenges import code_challenge15
            code_challenge15_help()
            while_loops()
      elif while_loops_choice == "5":
            loops_choice_option2()
      else:
            print("Invalid Choice")

def lists_menu():
      print("""
      ACCESSING MENU FOR LISTS
      Lists are used to store multiple items in a single variable.
      Choose from the options below:
            
      1. How does it work?
      2. Sample programs
      3. Return 
      """)
      list_menu_choice = input("Enter your choice: ")
      lists_menu_option(list_menu_choice)
      return list_menu_choice

def lists_menu_option(list_menu_choice):
      if list_menu_choice == "1":
            list_option1()
      elif list_menu_choice == "2":
            list_option2()
      elif list_menu_choice == "3":
            main_menu()
      else:
            print("Invalid Choice")


def list_option1():
      print("""
      List items are ordered, changeable, and allow duplicate values.
      List items are indexed, the first item has index [0], the second item has index [1] etc.
            
      Ordered
      When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
      If you add new items to a list, the new items will be placed at the end of the list.
      
      Changeable
      The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
      """)
      lists_menu()

def list_option2():
      print("""   
      You're accessing sample programs using loops 
      Choose from the option below:
            
      1. Fruits list
      2. Return
      """)
      list_option2_choice = input("Enter your choice: ")
      list_sampleprograms(list_option2_choice)
      return list_option2_choice

def list_sampleprograms(list_option2_choice):
      if list_option2_choice == "1":
            from Activities import activity25
            activity25_help()
            list_option2()
      elif list_option2_choice == "2":
            lists_menu()
      else:
            print("Invalid Choice")

def function_menu():
      print("""
      ACCESSING MENU FOR FUNCTIONS 
            
      A function is a block of code which only runs when it is called.
      You can pass data, known as parameters, into a function.
      A function can return data as a result.
            
      Choose from the option below:
      1. How does it works?
      2. Sample programs
      3. Return
      """)
      function_menu_choice = input("Enter your choice: ")
      function_menu_option(function_menu_choice)
      return function_menu_choice

def function_menu_option(function_menu_choice):
      if function_menu_choice == "1":
            function_option1()
      elif function_menu_choice == "2":
            function_option2()
      elif function_menu_choice == "3":
            main_menu()
      else:
            print("Invalid Choice")

def function_option1():
      print("""
      Creating a Function
      In Python a function is defined using the def keyword:
            def my_function():
                   print("Hello from a function")
            
      Calling a Function
      To call a function, use the function name followed by parenthesis:
            def my_function():
                   print("Hello from a function")

            my_function()

      Arguments
      Information can be passed into functions as arguments.
      Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
      The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
            def my_function(fname):
                  print(fname + " Refsnes")

            my_function("Emil")
            my_function("Tobias")
            my_function("Linus")   
                  """)
      function_menu()

def function_option2(): 
      print("""
      You're Accessing the sample programs using functions
      
      1. Simple menu
      2. Factorial
      3. Grocery program
      4. Return
      """)
      f_option2_choice = input("Enter your choice: ")
      function_sampleprograms(f_option2_choice)
      return f_option2_choice

def function_sampleprograms(f_option2_choice):
      if f_option2_choice == "1":
            from Activities import activity22
            activity22_help()
            function_option2()
      elif f_option2_choice == "2":
            from Activities import activity23
            activity23_help()
            function_option2()
      elif f_option2_choice == "3":
            from code_challenges import code_challenge16
            code_challenge16_help()
            function_option2()
      else:
            print("Invalid Choice")

print("Final Project for ITCS102 by John Kevin Aguilera")
strt = input("Would you like to access the program? (y/n): ")
if strt.lower() == "y":
      start()
elif strt.lower() == "n":
      print("Thank you for coming, You may now close the program. ")
      sys.exit()
else:
      print("Invalid choice, Please try again.")