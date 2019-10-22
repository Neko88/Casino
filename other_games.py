import random

def roulette(bet: str,number: int) -> bool:
  """
  Returns if the user's bet is correct in a simulation of roulette
  """
  #Outcomes
  red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
  black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
  column_one = [1,4,7,10,13,16,19,22,25,28,31,34]
  column_two = [2,5,8,11,14,17,20,23,26,29,32,35]
  column_three = [3,6,9,12,15,18,21,24,27,30,33,36] 

  #Roll and print outcome
  outcome = random.randint(0,37)  
  
  if outcome == 37:
    print("The number is 00")
  else:
    print("The number is " + str(outcome))

  #Singles 35 - 1 
  if bet == "Single":
    return number == outcome

  #Colours 1 - 1
  elif bet == "Red":
    return outcome in red

  elif bet == "Black":
    return outcome in black

  #Dozens 2 - 1
  elif bet == "Dozen 1":
    return 1 < outcome >= 12
  
  elif bet == "Dozen 2":
    return 13 <= outcome <= 24
  
  elif bet == "Dozen 3":
    return 25 <= outcome < 37

  #Highlow 1 - 1
  elif bet == "First 18":
    if outcome == 0 or outcome == 37:
      return False

    return outcome <= 18
  
  elif bet == "Last 18":
    if outcome == 0 or outcome == 37:
      return False

    return outcome >= 19

  #Even/Odd 1 - 1
  elif bet == "Even":
    if outcome == 0 or outcome == 37:
      return False

    return outcome % 2 == 0

  elif bet == "Odd":
    if outcome == 0 or outcome == 37:
      return False
      
    return outcome % 2 == 1
  
  #Column 2 - 1
  elif bet == "Column 1":
    return outcome in column_one
  
  elif bet == "Column 2":
    return outcome in column_two 

  elif bet == "Column 3":
    return outcome in column_three

  
  return False

def high_low(guess: str) -> bool:
  """
  Returns if guess is correct when comparing num and roll

  >>> high_low("low")
  roll = 10
  True
  >>> high_low("high")
  roll = 90
  False
  >>> high_low("high")
  roll = 50
  False
  """

  #Creates and print outcome
  roll = random.randint(1,100)
  print ("You rolled a " + str(roll))

  #Check if user's guess is correct
  if 50 > roll and guess == "high":
    return True

  elif 50 < roll and guess == "low":
    return True

  return False

def craps(shooter_outcome: str) -> str:
  """
  Returns if the player guesses correctly in a simulation of the game Craps

  >>> craps("Win")
  die1 = 1
  die2 = 2
  total = 3
  "lose"
  >>> craps("Win")
  die1 = 4
  die2 = 3
  total = 7
  "win"
  >>> craps("Lose")
  die1 = 6
  die2 = 6
  total = 12
  "tie"
  """
  #Variables for the game
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
  breakout = True

  #Print the outcome
  print("your rolls are: " + str(die1) + "," + str(die2))
  print("The total is " + str(total))
  print()
  
  #Comeout roll results
  #If the roll is a natural
  if total == 7 or total == 11:
    if shooter_outcome == "Win":
      return "Win"
    return "Lose"

  #If the roll is a crap
  elif total <= 3:
    if shooter_outcome == "Win":
      return "Lose"
    return "Win"

  #If the roll is a push 
  elif total == 12:
    return "Tie"

  #If the roll was something other than the rolls above
  point = total
  print("Your point is " + str(point))
  print()

  #Played until the outcome is either the number they rolled in the come out or is 7
  while breakout:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2

    print("your rolls are: " + str(die1) + "," + str(die2))
    print("The total is " + str(total))
    print()

    if total == 7:
      if shooter_outcome == "Win":
        return "Lose"
      return "Win"

    elif total == point:
      if shooter_outcome == "Win":
        return "Win"
      return "Lose"