import card_game
import other_games
import os
import roulette
from termcolor import *

def login_delete(lists, ld):
  user_user = input("Enter username: ")
  count = 1
  marker = 0 

  #Checks is username in database
  while len(lists) > count:
    if user_user == lists[count][:len(user_user)]:
      marker = count
      count = len(lists)    

    count += 1

  print("=====")

  if marker == 0:
    print("User not in database")
    return 0

  else:
    logs = lists[marker].split(",")

    user_pass = input("Enter password: ")

    while user_pass != logs[1]:
      print("Passwords do not match")
      print("=====")
      user_pass = input("Enter password or enter # to leave : ")

      if user_pass == "#":
        print("Leaving")
        return 0

    os.system('clear')

    if ld == "login":
      print("User has logged in")
    else:
      print("User is deleted")

    return marker

def account_creation(lists) -> None:
    #Username
    valid_user = False
    print("Your name can only include alphanumeric characters.")
    name = input("Enter your username: ")
    while not valid_user:
      #If not valid username
      if name.isalnum():
        valid_user = True
      
      #If not the only account
      if len(lists) > 1:
        in_database = True
        for i in range(1, len(lists)):          
          if lists[i][0:lists[i].find(",")] == name:
            in_database = False
            valid_user = False
      
      #Checkers
      if not in_database:
        print("=====")
        print("User is already in database.")
        name = input("Enter your username: ")

      elif not valid_user:
        print("=====")
        print("Enter a valid username.")
        name = input("Enter your username: ")      

    #Password
    print("=====")
    print("Your password can only include alphanumeric characters.")
    print("Your password must also have a mimnimum length of 8.")
    password = input("Enter your password: ")

    while len(password) < 8 or not password.isalnum():      
      print("=====")
      print("Password is invalid.")
      password = input("Enter your password: ")

    #Reenter password
    os.system('clear')  
    re_enter = input("Reenter your password or enter ""#"": ")

    while re_enter != password:
      if re_enter == "#":
        print("Account not created")
        print("=====")
        return

      os.system('clear')
      print("Passwords do not match")      
      re_enter = input("Reenter your password or enter ""#"": ")
      
    os.system('clear')
    
    lists[0] = "0\n"
    lists.append(name + "," + password + "," + "200\n")
    print("Account created. Account contains $200 on the house.")
    print("Login in to continue")
    print("=====")

def selector() -> str:
    print("Continue: 0")
    print("Log out: 1")
    print("Create a new account: 2")
    print("Log into a different account: 3")
    print("Delete account: 4")
    print("Exit: 5")

    return input("Select 1 of the above to continue: ")
    print("=====")

def greeter(user_info):
  print("Greetings " + user_info[0] + ".")
  print("You have $" + user_info[2].strip() + ".")
  print("=====")


def bet_maker(cash):
  bet = input("Enter your bet amount: ")

  if not bet.isnumeric() or int(bet) > cash or int(bet) <= 0:
    print("Enter a valid bet amount.")
    return -1

  return int(bet)

def bet_outcome(cash):
  if cash == 0:
    print("No changes were made to your balance")
  elif cash > 0:
    print("You have gained $" + str(cash) + ".")
  else:
    print("You have lost $" + str(-1 * cash) + ".")
  

def ui() -> None:
  #Files
  reader = open("data.txt", "r")
  info = reader.readlines()  
  reader.close()

  writer = open("data.txt", "w")

  #No accounts
  if len(info) == 1:
    print("There are no accounts open at this current moment.")
    print("Please create one to continue.")
    account_creation(info)

  iden = int(info[0].strip())

  #No logged in account
  while iden == 0:
    logged_in = False
    while not logged_in:
      print("No user has logged in.")
      print("Login in or create a new account to continue")
      print("Login: 1")
      print("Create account: 2")
      log_acc = input("Select 1 to continue: ")     

      while not(log_acc == "1" or log_acc == "2"):
        print("Enter a valid input")
        log_acc = input("Select 1 to continue: ")
      
      if log_acc == "2":
        account_creation(info)

      else:
        iden = login_delete(info, "login")

        if iden != 0:
          logged_in = True

      
    info[0] = str(iden) +"\n"
    print("=====")

  user_info = info[iden].split(",")
  greeter(user_info)

  #User select
  exited = True
  decision = selector()

  if decision == "5":
    print("Exiting of casino...")
    exited = False  

  while exited:
    #Continue
    if decision == "0":
      cash = int(user_info[2].strip())
      old = cash

      play = "0"

      while play != "5":
        print("=====")
        print("You have $" + str(cash) + ".")
        print("Backjack: 1")
        print("Craps: 2")
        print("Roulette: 3")
        print("Highlow: 4")
        print("Exit: 5")

        play = input("Select the game you want to play: ")
        print("=====")

        bet = 0

        if play == "1":
          bet = bet_maker(cash)

          if bet != -1:  
            bet = card_game.black_jack(bet)
            bet_outcome(bet)          
            cash += bet

            if cash <= 0:
              print("You do not have anymore money.")        
              print("Account will now be deleted.")
              print("=====")

              info[-1], info[iden] = info[iden], info[-1]
              info = info[:-1]

              play = "5"
              exited = False
              iden = 0
              info[0] = "0\n"

        elif play == "2":
          bet = bet_maker(cash)

          if bet != -1:  
            guess = input("Enter if shooter will win or lose. input 'Win' for shooter win and anything else for shooter lose: ")
            bet = other_games.craps(guess, bet)
            bet_outcome(bet)
            cash += bet

            if cash <= 0:
              print("You do not have anymore money.")        
              print("Account will now be deleted.")
              print("=====")

              info[-1], info[iden] = info[iden], info[-1]
              info = info[:-1]

              play = "5"
              exited = False
              iden = 0
              info[0] = "0\n"

        elif play == "3":
          bet = bet_maker(cash)

          if bet != -1:
            roulette.table()
            guess = roulette.choices()
            if guess[-1] == 1:
              bet = other_games.roulette(guess[0], bet, guess[1])
              bet_outcome(bet)
              cash += bet
              if cash <= 0:
                print("You do not have anymore money.")        
                print("Account will now be deleted.")
                print("=====")

                info[-1], info[iden] = info[iden], info[-1]
                info = info[:-1]

                play = "5"
                exited = False
                iden = 0
                info[0] = "0\n"
            

          print("=====")

        elif play == "4":
          bet = bet_maker(cash)
          if bet != -1:
            guess = input("Enter if the number will be 'high' or 'low' than 50: ")
            bet = other_games.high_low(guess, bet)
            bet_outcome(bet)
            cash += bet

            if cash <= 0:
              print("You do not have anymore money.")        
              print("Account will now be deleted.")
              print("=====")

              info[-1], info[iden] = info[iden], info[-1]
              info = info[:-1]

              play = "5"
              exited = False
              iden = 0
              info[0] = "0\n"

        elif play == "5":
          print("You have $" + str(cash) + ".")
         
        else:
          print("Enter a valid input")

      if old != cash and iden != 0:
        user_info[2] = str(cash)
        infos = ""

        for i in user_info:
          infos += i + ","

        info[iden] = infos[:-1] + "\n"

      if iden != 0:
        decision = selector()

    #Log out
    elif decision == "1":
      info[0] = "0\n"
      exited = False
      print("=====")
      print("Logging out...")
      print("Program will now close")

    #Create account
    elif decision == "2":
      account_creation(info)
      decision = selector()
    
    #Log into different account
    elif decision == "3":
      info[0] = str(login_delete(info, "login")) +"\n"
      iden = int(info[0].strip())
      user_info = info[iden].split(",")

      greeter(user_info)

      decision = selector()

    #Delete account
    elif decision == "4":
      print("Enter the valid information to delete the account")
      delete = login_delete(info, "delete")
      if delete == 0:
        os.system('clear')
        print("Account not deleted")
      else:
        info[delete], info[-1] = info[-1],info[delete]
        info = info[0:-1]

      #If no more acocunts
      if len(info) == 1:
        print("No more accounts left, exiting program.")
        info[0] = 0

      else:
        decision = selector()      

    #Leave
    elif decision == "5":
      print("Exiting of casino...")
      exited = False

    #Invalid selection
    else:
      print("Enter a valid input to continue")
      print("=====")
      decision = selector()


  #Writes to file all users
  for i in range(0, len(info)):
    writer.write(info[i])
  
  writer.close()

if __name__ == "__main__":
  ui()

  