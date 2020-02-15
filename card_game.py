import cards 
import random

def black_jack(bet: int) -> int:
  """
  Simulates a game of blackjack
  """
  #Creates and shuffle deck
  deck = cards.deck_of_cards()
  random.shuffle(deck)    

  #Variables for the game
  users_hand = []
  has_ace = 0 
  users_total = 0  
  
  dealers_hand = []
  dealers_ace = 0
  dealers_total = 0

  #Draw cards
  users_hand.append(cards.draw(deck))
  users_hand.append(cards.draw(deck))

  dealers_hand.append(cards.draw(deck))
  dealers_hand.append(cards.draw(deck))
  
  #Identifies Aces
  for i in users_hand:
    if i[0:3] == "Ace":
      has_ace += 1
  for i in dealers_hand:
    if i[0:3] == "Ace":
      dealers_ace += 1

  #Create help to identify and add value of card
  users_total = cards.recognize_numberbj(users_hand[0]) + cards.recognize_numberbj(users_hand[1])

  dealers_total = cards.recognize_numberbj(dealers_hand[0]) + cards.recognize_numberbj(dealers_hand[1])

  #If hand has two aces
  if users_total > 21:
    users_total = users_total - 10
    has_ace = has_ace - 1
  if dealers_ace > 21:
    dealers_total = dealers_total - 10
    dealers_ace = dealers_ace - 1

  #Show draws
  print("User's hand: ", end = "")
  print(users_hand)
  print("User's total: " + str(users_total))
  print()

  print("Dealer's hand: ", end = "")
  print("['" + dealers_hand[0] + "', 'Hidden Card']")
  print("Dealer's total: " + str(cards.recognize_numberbj(dealers_hand[0])))
  print("========================================")
  
  #Outcome of deal
  #If you have natural
  if users_total == 21:
    print("You have a natural so it is time to reveal the dealer's hand")
    print("Dealer's hand: ", end = "")
    print(dealers_hand)
    print("Dealer's total: " +  str(dealers_total))

    if dealers_total == 21:
      print("It is a tie!")
      return 0
    print("You Win!")
    return bet

  #Otherwise
  else:
    #Player's turn
    while input("Hit or Stay: ") != "Stay":
      #Draw Card
      users_hand.append(cards.draw(deck))
      users_total += cards.recognize_numberbj(users_hand[-1])

      if cards.recognize_numberbj(users_hand[-1]) == 11:
        has_ace += 1

      #Check if user has ace if total over 21
      if users_total > 21 and has_ace != 0:
        users_total = users_total - 10
        has_ace = has_ace - 1

      #Prints out result
      print("User's hand: ", end = "")
      print(users_hand)
      print("User's total: " + str(users_total))
      print()

      #User busted
      if users_total > 21:
        print("You are busted")
        return bet * -1

    #Dealer's turn
    print("========================================")
    print ("You stayed so now it's time for the dealer")
    print("Dealer's hand: ", end = "")
    print(dealers_hand)
    print("Dealer's total: " +  str(dealers_total))
    print()
    
    while dealers_total < 17:
      #Draw card
      dealers_hand.append(cards.draw(deck))
      dealers_total += cards.recognize_numberbj(dealers_hand[-1])

      if cards.recognize_numberbj(dealers_hand[-1]) == 11:
        dealers_ace += 1

      #Check if dealer has ace given total is over 21
      if dealers_ace != 0 and dealers_total > 21:
        dealers_total = dealers_total - 10
        dealers_ace = dealers_ace - 1

      #Reveal outcome
      print("Dealer's hand: ", end = "")
      print(dealers_hand)
      print("Dealer's total: " +  str(dealers_total))
      print()

      #If dealer busted
      if dealers_total > 21:
        print("Dealer has busted")
        return bet

    print("========================================")

    #If dealer and user stayed
    if dealers_total == users_total:
      print("Both hands are equal. It's a tie.")
      return 0

    if dealers_total > users_total:
      print("Dealer has the higher hand. You lose.")
      return bet * -1

    print("You have the higher hand. You win!")
    return bet
