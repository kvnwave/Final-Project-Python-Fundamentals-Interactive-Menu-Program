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