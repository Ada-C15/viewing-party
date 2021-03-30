from random import randrange

number = randrange(10)

guess = -1
while number != guess:
  guess = int(input('Please enter a guess between 0-10  ==>'))
  if guess < number:
    print(f"{guess} is too low")
  elif number > guess:
    print(f"{guess} is too high")
  else:
    print("You guessed it!")