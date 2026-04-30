import random
from words import wordList

hangman = {0:("   ","   ","   "),
           1:(" o ","   ","   "),
           2:(" o "," | ","   "),
           3:(" o ","/| ","   "),
           4:(" o ","/|\\ ","   "),
           5:(" o ","/|\\ ","/  "),
           6: (" o ","/|\\ ","/ \\")}
def displayMan(wrongGuesses):
  print("****************")
  for line in hangman[wrongGuesses]:
    print(line)
  print("****************")
def displayHint(hint):
  print(" ".join(hint))
def displayAnswer(answer):
  print(" ".join(answer))
def main():
  answer = random.choice(wordList).lower()
  hint = ["_"] * len(answer)
  wrongGuesses = 0
  alreadyGuessed = set()
  isRunning = True

  while isRunning:
    displayMan(wrongGuesses)
    displayHint(hint)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input")
      continue

    if guess in alreadyGuessed:
      print(f"{guess} is already guessed")
      continue

    alreadyGuessed.add(guess)
    
    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          hint[i] = guess
    else:
      wrongGuesses += 1
    
    if "_" not in hint:
      displayMan(wrongGuesses)
      displayAnswer(answer)
      print("You win!")
      isRunning = False
    elif wrongGuesses >= len(hangman) - 1:
      displayMan(wrongGuesses)
      displayAnswer(answer)
      print("You lose!")
      isRunning = False

if __name__ == '__main__':
  main()