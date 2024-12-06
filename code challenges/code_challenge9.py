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