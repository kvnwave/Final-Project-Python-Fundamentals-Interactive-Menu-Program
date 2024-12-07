print("--- PYTHON PROGRAM ---") #replace nalang
user = input("Before accessing the program, we will need to know your name\nInput it here: ")
print(f"Hello {user}, You may now access the program")

def main_menu(): #main menu
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
      choice = input("Enter your choice: ")
      return choice

def print_statements_option1():
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

def process(choice):
      if choice == "1":
            print_statements_menu_option = print_statements_menu()
      elif choice == "2":
            variable_menu_option = variables_menu()
      elif choice == "3":
            operators_menu_option = operators_menu()
      elif choice == "4":
            pass
      elif choice == "5":
            pass
      elif choice == "6":
            pass
      elif choice == "7":
            pass
      elif choice == "8":
            pass
      else:
            print("Invalid Choice, Please try again")

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

isContinue = True

while isContinue:
      main_menu_choice = main_menu()      
      process(main_menu_choice)
      if main_menu_choice == "8":
            print("Program Terminated.")
            break