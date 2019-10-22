def recognize_number(card: str) -> int:
  """
  Returns a number based on the first and possibly second character of card

  Precondtion: length of card is at least 2

  >>> recognize_number("Ace of hearts")
  1
  >>> recognize_number("King of spades")
  13
  >>> recognize_number("2 of clubs")
  2
  >>> recognize_number("Wrong card")
  0
  """
  identify = card[:2]

  #If the card is a number
  if identify[0].isnumeric():
    if identify[1].isnumeric():
      return 10
    return int(identify[0])

  #If the card is a face card
  if identify[0] == "A":
    return 1
  elif identify[0] == "J":
    return 11
  elif identify[0] == "Q":
    return 12
  elif identify[0] == "K":
    return 13

  return 0