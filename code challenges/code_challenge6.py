
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