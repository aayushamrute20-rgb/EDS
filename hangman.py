import random
from words import wordList

def displayHangman(wrong):
    if wrong == 0:
      print("**************\n**************")
    else:
      print("**************")
      for i in range(len(hangMan[wrong-1])):
        print(hangMan[wrong-1][i])
      print("**************")
def check(guess,inrandomWord):
  for i in range(len(inrandomWord)):
    if guess == inrandomWord[i]:
      return -1
def playAgain(cmnd):
  if cmnd.upper() == "Y":
    main()
def updatehint(guess):
  global randomWord,hint
  for i in range(len(randomWord)):
    if randomWord[i] == guess:
      hint[i] = guess

print("Complete the Word before the hangman appears!!")
hangMan = ((" o ",),
           (" o "," |"),
           (" o ","/|"),
           (" o ","/|\\"),
           (" o ","/|\\","/ "),
           (" o ","/|\\","/ \\"))
def main():
  global hint,randomWord
  alreadyGuessed = []
  randomWord = [letters.lower() for letters in random.choice(wordList)]
  hint = ["_" for _ in randomWord]
  wrongGuess = 0

  while wrongGuess<6 and hint != randomWord:
    displayHangman(wrongGuess)
    print(" ".join(hint))
    guess = input("Guess: ").lower()
    
    if check(guess,alreadyGuessed) == -1 and check(guess,randomWord) == -1:
     print("Letter already guessed")
    else:
      if check(guess,randomWord) == -1:
        updatehint(guess)
      elif len(guess) != 1:
        print("Please enter only one letter!!")
      elif not guess.isalpha():
        print("Invalid input, please enter a letter!!")
      else:
        wrongGuess += 1
        print("Wrong guess!")
        

    alreadyGuessed.append(guess)
  
  if wrongGuess == 6:
    print("--------------")
    print(f"The word was: {"".join(randomWord)}\nYou Lost,Game Over!!")
    print("--------------")
  else:
    print("--------------")
    print("   You Won!!  ")
    print("--------------")
 
  cmnd = input("Do you want to play again? (Y/N): ")
  playAgain(cmnd)

if __name__ == '__main__':
  main()
