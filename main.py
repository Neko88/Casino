import card_game
import other_games


def ui() -> None:
  """
  To create a ui in order to utilize the functions 
  """
  user_input = ""
  outcome = ""
  
  print("""
  1 - Craps 
  2 - Highlow 
  3 - Black Jack
  4 - Roulette  
  """)

  user_input = int(input("Select a choice above: "))
  print("========================================")

  if user_input == 1:
    outcome = other_games.craps(input("Will the shooter 'Win' or 'Lose': "))    

    if outcome == "Win":
      print("You win!")
    elif outcome == "Lose":
      print("You lose")  
    else:
      print("It's a tie!")
    print("========================================")

  elif user_input == 2:
    outcome =  other_games.high_low(input("Will it be 'high' or 'low' than 50?: "))
    print()  

    if outcome:
      print("You win!")
    else:
      print("You lose")  
    print("========================================")
  
  elif user_input == 3:
    outcome = card_game.black_jack()
  
  elif user_input == 4:
    outcome = other_games.roulette(input("Enter bet type: "), int(input("Enter number if required: ")))
    print()

    if outcome:
      print("You win!")
    else:
      print("You lose")
    print("========================================")

ui()

  