def deck_of_cards():
  """
  Returns a list that mimics a deck of cards  
  """
  suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
  values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",]
  deck = []

  for i in suits:
    for j in values:
      deck.append(j + " of " + i)

  return deck

def recognize_numberbj(card: str) -> int:
  """
  Returns a number based on card's value in blackjack
  >>> recognize_numberbj("Ace of hearts")
  11
  >>> recognize_numberbj("King of spades")
  10
  >>> recognize_numberbj("2 of clubs")
  2
  >>> recognize_numberbj("Wrong card")
  10
  """
  identify = card[:4]

  #If the card is a number
  if identify[0].isnumeric():
    if identify[1].isnumeric():
      return 10
    return int(identify[0])

  #If card is an ace
  if identify[0:3] == "Ace":
    return 11

  #If the card is a face card
  return 10

def draw(deck) -> str:
  """Returns the first index of deck  that has a value while removing said value

  Precondtion: deck is a string list

  >>>draw(["1","2","3"])
  "1"
  >>>draw([null,"s"])
  "s"
  >>>draw([null,null])
  "null"
  """
  holder = ""

  for i in range(len(deck)):
    if deck[i] != "null":
      holder, deck[i] = deck[i], "null"
      return holder
  return "null"  