from termcolor import *

#Table
from termcolor import *

def rowcolor(nums, start):
  if start == 'red':
    nums_colors = ['red', 'grey', 'red']
  else:
    nums_colors = ['grey', 'red', 'grey']
  
  for i in range(2):
    if nums_colors[i] == 'grey':
      print(colored(nums[i], nums_colors[i], 'on_white'), end = " ")
    else:
      print (colored(nums[i], nums_colors[i]), end = " ")
    print ("| ", end = "")

  if nums_colors[-1] == "red":
    print(colored(nums[-1], nums_colors[-1]))
  else:
    print(colored(nums[-1], nums_colors[-1], "on_white"))

def rowcolor_free(nums, color):
  for i in range(2):
    if color[i] == "grey":
      print(colored(nums[i], color[i], "on_white"), end = "")
    else:
      print(colored(nums[i], color[i]), end = "")
    print("| ", end = "")
  
  if color[-1] == "red":
    print(colored(nums[-1], color[-1]))
  else:
    print(colored(nums[-1], color[-1], "on_white"))

def add_row(row):
  print("Row " + str(row) + ": " , end = "")
  return row +1

def table():
  print(colored("          0", 'green'), end =" ")
  print("| ", end = "")
  print(colored("00", 'green'))

  row = 1
  r = "red"
  g = "grey"

  for i in range(1, 9, 3):
    row = add_row(row)
    print(" ", end = "")

    if i%2 == 1:
      rowcolor([i, i+1, i+2], "red")
    else:
      rowcolor([i, i+1, i+2], "grey")

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([10, 11, 12], [g, g, r])

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([13, 14, 15], [g, r, g])

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([16, 17, 18], [r, g, r])

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([19, 20, 21], [r, g, r])

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([22, 23, 24], [g, r, g])

  row = add_row(row)
  print(" ", end = "")
  rowcolor_free([25, 26, 27], [r, g, r])

  row = add_row(row)
  rowcolor_free([28, 29, 30], [g, g, r])

  row = add_row(row)
  rowcolor_free([31, 32, 33], [g, r, g])

  row = add_row(row)
  rowcolor_free([34, 35, 36], [r, g, r])

  print("        C1| C2| C3")


#Choices
def valid(lst, decision, num):
  lst[0] = decision
  lst[1] = int(num)
  lst[2] = 1

def choices():
  decision = [0,0,0]
  print("Singles: 1")
  print("Split: 2")
  print("Street: 3")
  print("Square: 4")
  print("Six: 5")
  print("Colour: 6")
  print("Dozen: 7")
  print("Halfs: 8")
  print("Even/Odd: 9")
  print("Columns: 10")

  pick = input("Enter an option from the above: ")
  if not pick.isnumeric() or not 1 <= int(pick) <= 10:
    print("Enter valid input")
      
  elif pick == "1":
    num = input("Enter a number between 0-36 or 37 for 00: ")
    if not num.isnumeric() or not 0 <= int(num) <= 37:
      print("Enter valid input")

    else:
      valid(decision, "Single", num)
  
  elif pick == "2":
    num = input("Enter the first number: ")
    if not num.isnumeric() or not 1 <= int(num) <= 36:
      print("Enter valid input")

    else:
      ver = input("Enter 1 if it is a split to the right or 2 if the split is downwards: ")
      if not ver.isnumeric() or not 1 <= int(ver) <= 2:
        print("Enter valid input")      

      else:
        if int(ver) == 1:
          if int(num) % 3 == 0:
            print("Enter valid input")

          else:
            valid(decision, "Split1", num)
        
        else:
          if 34 <= int(num) <= 36:
            print("Enter valid input")

          else:
            valid(decision, "Split2", num)
  
  elif pick == "3":
    num = input("Enter the row you want to bet on: ")
    if not num.isnumeric() or not 1 <= int(num) <= 12:
      print("Enter valid input")
    else:
      valid(decision, "Street", num)
  
  elif pick == "4":
    num = input("Enter the top left of the square: ")
    if not num.isnumeric() or not int(num)%3 == 0 or not 34 <= int(num) <= 36:
      print("Enter valid input")
    else:
      valid(decision, "Square", num)
  
  elif pick == "5":
    num = input("Enter the top left of the six numbers: ")
    if not num.isnumeric() or not (int(num)-1)%3 == 0 or int(num) == 34:
      print("Enter valid input")

    else:
      valid(decision, "Six", num)
    
  elif pick == "6":
    num = input("Enter 'Black' or 'Red': ")
    if num == "Black":
      valid(decision, "Black", 0)

    else:
      valid(decision, "Red", 0)
    
  elif pick == "7":
    num = input("Enter 1, 2, or 3 to pick column 1, 2, or 3 respectivley: ")

    if num.isnumeric() or not 1 <= int(num) <= 3:
      print("Enter valid input")

    else:
      valid(decision,"Dozen " + num, 0)
    
  elif pick == "8":
    num = input("Enter 1 for 1 - 18 or 2 for 19 - 36: ")

    if not num.isnumeric() or not 1 <= int(num) <= 2:
      print("Enter valid input")
      
    elif num == "1":
      valid(decision, "1 - 18", 0)

    else:
      valid(decision, "19 - 36", 0)
    
  elif pick == "9":
    num = input("Enter 1 for even or 2 for odd: ")
    if not num.isnumeric() or not 1 <= int(num) <= 2:
      print("Enter valid input")
      
    elif num == "1":
      valid(decision, "Even", 0)

    else:
      valid(decision, "Odd", 0)
    
  elif pick == "10":
    num = input("Enter 1, 2, or 3 for the coresponding column: ")
    if not num.isnumeric() or not 1 <= int(num) <= 3:
      print("Enter valid input")
      
    else:
      valid(decision, "Column " + num, 0)

  return decision
    

