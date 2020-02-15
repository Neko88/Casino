import random

def roulette(bet: str, money: int, number = None) -> int:
  """
  Returns if the user's bet is correct in a simulation of roulette
  """
  #Outcomes
  red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
  black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
  column_one = [1,4,7,10,13,16,19,22,25,28,31,34]
  column_two = [2,5,8,11,14,17,20,23,26,29,32,35]
  column_three = [3,6,9,12,15,18,21,24,27,30,33,36] 
  users = []

  #Roll and print outcome
  outcome = random.randint(0,37)  
  
  if outcome == 37:
    print("The number is 00")
  else:
    print("The number is " + str(outcome))

  #Singles 35 - 1 
  if bet == "Single":
    if outcome == int(number):
      return money * 35

    else:
      return -1 * money

  #Splits 17 - 1
  if "Split" in bet:
    if "1" in bet:
      users = [number, number + 1]

    else:
      users = [number, number + 3]

    if outcome in users:
      return money * 17
  
  #Street 11 - 1
  if "Street" in bet:
    users = [number*3, number*3-1, number*3-2]
    if outcome in users:
      return money * 11

  #Square 8 - 1
  if "Square" == bet:
    users = [number, number+1, number+3, number+4]
    if outcome in users:
      return money * 8

  #Six 5 - 1
  if "Six" == bet:
    for i in range(6):
      users.append(number + i)

    if outcome in users:
      return money * 5

  #Colours 1 - 1
  elif bet == "Red":
    if outcome in red:
      return money

  elif bet == "Black":
    if outcome in black:
      return money
  
  #Dozens 2 - 1
  elif bet == "Dozen 1":
    if 1 < outcome <= 12:
      return money * 2
  
  elif bet == "Dozen 2":
    if 13 <= outcome <= 24:
      return money * 2

  elif bet == "Dozen 3":
    if 25 <= outcome < 37:
      return money * 2
  
  #Highlow 1 - 1
  elif bet == "1 - 18":
    if outcome == 0 or outcome == 37 or outcome >= 19:
      return money * -1

    return money
  
  elif bet == "19 - 36":
    if outcome == 0 or outcome == 37 or outcome <= 18:
      return money * -1

    return money

  #Even/Odd 1 - 1
  elif bet == "Even":
    if outcome == 0 or outcome == 37 or outcome % 2 == 1:
      return money * -1

    return money

  elif bet == "Odd":
    if outcome == 0 or outcome == 37 or outcome % 2 == 0:
      return money * -1

    return money 
  
  #Column 2 - 1
  elif bet == "Column 1":
    if outcome in column_one:
      return money * 2

  elif bet == "Column 2":
    if outcome in column_two:
      return money * 2

  elif bet == "Column 3":
    if outcome in column_three:
      return money * 2
  
  return money * -1

def high_low(guess: str, bet: int) -> int:
  """
  Returns if guess is correct when comparing num and roll

  """

  #Creates and print outcome
  roll = random.randint(1,100)
  print ("You rolled a " + str(roll))

  #Check if user's guess is correct
  if 50 < roll and guess == "high":    
    return bet

  elif 50 > roll and guess == "low":
    return bet

  return -1 * bet

def craps(shooter_outcome: str, bet: int) -> int:
  """
  Returns if the player guesses correctly in a simulation of the game Craps
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
    print("A natural!")
    if shooter_outcome == "Win":
      print("You guessed right!")
      return bet 
    print("You guessed wrong.")
    return bet * -1

  #If the roll is a crap
  elif total <= 3:
    print("It's a crap!")
    if shooter_outcome == "Win":
      print("You guessed wrong.")
      return bet * -1
    print("You guessed right!")
    return bet

  #If the roll is a push 
  elif total == 12:
    return 0

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
        print("You guessed wrong.")
        return bet * -1
      print("You guessed right!")
      return bet

    elif total == point:
      if shooter_outcome == "Win":
        print("You guessed right!")
        return bet
      print("You guessed wrong.")
      return bet * -1