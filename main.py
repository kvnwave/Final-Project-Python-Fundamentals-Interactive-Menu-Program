print("--- PYTHON PROGRAM ---") #replace nalang
user = input("Before accessing the program, we will need to know your name\nInput it here: ")

def main_menu(): #main menu
      print(f"""\nUser - {user}, Accessing - MENU
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
      print("""\tYou can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.
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
            pass
      elif choice == "3":
            pass
      elif choice == "4":
            pass
      elif choice == "5":
            pass
      elif choice == "6":
            pass
      elif choice == "7":
            pass
      else:
            print("Invalid Choice, Please try again")

isContinue = True

while isContinue:
      main_menu_choice = main_menu()      
      process(main_menu_choice)
      if main_menu_choice == "8":
            print("Program Terminated.")
            break
