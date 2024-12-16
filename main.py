# def menu():
#       isContinue = True

#       while isContinue:
#             main_menu_choice = main_menu()      
#             process(main_menu_choice)
#             if main_menu_choice == "8":
#                   # print("Program Terminated.")
#                   break
# import sys
# import atexit     

# def cleanup():
#     print("Program Terminated.")

def display_menu(): #main menu
      print(f"""
      =======================================================
        You're accessing MENU, Options are provided below =
         1 - print statements                              
         2 - variables                                     
         3 - operators                                     
         4 - conditional statements                        
         5 - loops                                        
         6 - lists                                         
         7 - functions                                     
         8 - exit                                          
      =======================================================   
      """)  
      # choice = input("Enter your choice: ")
      # return choice

def print_statements_option1(): # option 1 for print statement
      print()
      print("""\tHOW DOES PRINT WORK?
      You can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.
      Then, these parameters are represented as strings by their respective str() functions. To create a single output string, 
      the transformed strings are concatenated with spaces between them""")
      return print_statements_menu() 

def print_statements_option2(): 
      print()
      from Activities import activity1
      return print_statements_menu()

def print_statements_option3():
      return main_menu()

def print_statements_menu():
      print("\nACCESSING PRINT STATEMENTS MENU")
      print("\nPython print() function prints the message to the screen or any other standard output device.")
      print("\nChoose from options below:")
      print("1. How does it works?")
      print("2. Sample programs")
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

# def process(choice): # options for menu
#       if choice == "1":
#             print_statements_menu_option = print_statements_menu()
#       elif choice == "2":
#             variable_menu_option = variables_menu()
#       elif choice == "3":
#             operators_menu_option = operators_menu()
#       elif choice == "4":
#             conditionalstatements_menu_option = conditionalstatements_menu()
#       elif choice == "5":
#             loops_menu()
#       elif choice == "6":
#             pass
#       elif choice == "7":
#             pass
#       elif choice == "8":
#             print("Program Terminated")
#             return
#       else:
#             print("Invalid Choice, Please try again")

def main_menu():
      stop = False
      while stop != True:
            display_menu()  # Show the menu options
            choice = input("Enter your choice: ")
            if choice == "8":
                  stop == True
                  print("PROGRAM TERMINATED")
                  break
            elif choice == '1':
                  print("You chose option 1: Print statements.")
                  print_statements_menu()
            elif choice == '2':
                  print("You chose option 2: Variables.")
                  variables_menu()
            elif choice == '3':
                  print("You chose option 3: Operators.")
                  operators_menu()
            elif choice == '4':
                  print("You chose option 4: Conditional statements.")
                  conditionalstatements_menu()
            elif choice == '5':
                  print("You chose option 5: Loops.")
                  loops_menu()
            elif choice == '6':
                  print("You chose option 6: Lists.")
                  lists_menu()
            elif choice == '7':
                  print("You chose option 7: Functions.")
                  function_menu()
            # if choice == '8':
            #       # ask = input("Are you sure you want to exit? (y/n): ")
            #       # if ask.lower() == "y":
            #       #       break
            #       # elif ask.lower() == "n":
            #       #       continue
            #       # else:
            #       #       print("Invalid Choice, Please try again")
            #       #       continue
            #       break
            else:
                  print("Invalid choice. Please try again.")
        
def variables_menu():
      print("""ACCESSING VARIBLES MENU
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
            return main_menu()

def variable_choice_option1():
      print("""HOW DOES VARIABLES WORK?
      In Python, variables are symbolic names that refer to objects or values stored in your computer’s memory. 
      They allow you to assign descriptive names to data, making it easier to manipulate and reuse values throughout your code.

      Understanding variables is key for Python developers because variables are essential building blocks for any Python program. 
      Proper use of variables allows you to write clear, readable, and maintainable code.
""")
      return variables_menu()

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
      return variables_menu()
def variable_sampleprogram(variable_sampleprogramchoice):
      if variable_sampleprogramchoice == "1":
            from Activities import activity3_aguilera
            return variable_choice_option2()
      if variable_sampleprogramchoice == "2":
            from code_challenges import code_challenge2
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
      return operators_menu()

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
            return  operators_choice_option2()
      elif operators_sampleprogramchoice == "2":
            from code_challenges import code_challenge5
            return operators_choice_option2()
      elif operators_sampleprogramchoice == "3":
            from Activities import activity6
            return operators_choice_option2()
      elif operators_sampleprogramchoice == "4":
            from code_challenges import code_challenge4
            return operators_choice_option2()
      elif operators_sampleprogramchoice == "5":
            return operators_menu()
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
            return main_menu()

def conditionalstatements_option1():
      print("""
      In Python, conditional statements allow you to execute different blocks of code based on certain conditions. 
      The most common types of conditional statements are if, elif (else if), and else. 
      These statements enable decision-making in your program.
      """)
      return conditionalstatements_menu()

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
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "2":
            from Activities import activity8
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "3":
            from Activities import activity9
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "4":
            from Activities import activity10
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "5":
            from code_challenges import code_challenge6
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "6":
            from code_challenges import code_challenge7
            return conditionalstatements_option2()
      elif  conditionalstatements_option2_choice == "7":
            return conditionalstatements_menu()
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
            return main_menu()
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
      return loops_menu()

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
            return loops_menu()
      else:
            print("Invalid Choice")

def for_loops(): 
      print("""
      You're accessing For loop sample programs
      Choosee from the option below:
            
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
            return for_loops()
      elif for_loops_choice == "2":
            from Activities import activity12
            return for_loops()
      elif for_loops_choice == "3":
            from Activities import activity13
            return for_loops()
      elif for_loops_choice == "4":
            from Activities import activity14
            return for_loops()
      elif for_loops_choice == "5":
            from Activities import activity15
            return for_loops()
      elif for_loops_choice == "6":
            from Activities import activity17
            return for_loops()
      elif for_loops_choice == "7":
            from Activities import activity18
            return for_loops()
      elif for_loops_choice == "8":
            from code_challenges import code_challenge8
            return for_loops()
      elif for_loops_choice == "9":
            from code_challenges import code_challenge9
            return for_loops()
      elif for_loops_choice == "10":
            from code_challenges import code_challenge10
            return for_loops()
      elif for_loops_choice == "11":
            from code_challenges import code_challenge11
            return for_loops()
      elif for_loops_choice == "12":
            from code_challenges import code_challenge12
            return for_loops()
      elif for_loops_choice == "13":
            from code_challenges import code_challenge13
            return for_loops()
      elif for_loops_choice == "14":
            return loops_choice_option2()
      else:
            print("Invalid Choice")

def while_loops(): # 19 20 cc14 cc15
      print("""
      You're accessing While loop sample programs
      Choosee from the option below:
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
            return while_loops()
      elif while_loops_choice == "2":
            from Activities import activity20
            return while_loops()
      elif while_loops_choice == "3":
            from code_challenges import code_challenge14
            return while_loops()
      elif while_loops_choice == "4":
            from code_challenges import code_challenge15
            return while_loops()
      elif while_loops_choice == "5":
            return loops_choice_option2()
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
            return main_menu()
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
      return lists_menu()

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
            return list_option2()
      elif list_option2_choice == "2":
            return lists_menu()
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
            return main_menu()
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
      return function_menu()

def function_option2(): # 22 23 cc16
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
            return function_option2()
      elif f_option2_choice == "2":
            from Activities import activity23
            return function_option2()
      elif f_option2_choice == "3":
            from code_challenges import code_challenge16
            return function_option2()
      else:
            print("Invalid Choice")
     
# isContinue = True

# while isContinue:
#       main_menu_choice = main_menu()      
#       process(main_menu_choice)
#       if main_menu_choice == "8":
#             print("Program Terminated.")
#             break

print("--- PYTHON PROGRAM ---") #replace nalang
user = input("Before accessing the program, we will need to know your name\nInput it here: ")
print(f"Hello {user}, You may now access the program")
main_menu()