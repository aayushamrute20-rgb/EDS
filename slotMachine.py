import random as rd
import time as t

def spin():
 del slot[:]
 for i in range(3):
    slot.append(rd.choice(symbols))
 print("Spinning....")
 print("__________\n")
 for j in slot:
    print(j,end =' ')
    t.sleep(0.1)
 print("\n__________")
def reward():
  global balance
  if slot[0] == slot[1] == slot[2]:
      if slot[0] == '⭐️':
       balance += bet * 10
       return "Congratulations you won stars!!"
      elif slot[0] == '🍒':
       balance += bet * 2
       return "Congratulations you won cherries!!"
      elif slot[0] == '🍋':
       balance += bet * 10
       return "Congratulations you won lemons!!"
      elif slot[0] == '🍉':
       balance += bet * 5
       return "Congratulations you won watermelons!!"
      elif slot[0] == '🍇':
       balance += bet * 100
       return "Congratulations!! you got a Jackpot!!"
  else:
    return "***Better luck next Time***"
def checkBet():
    global bet
    bet = int(input("Enter your bet amount: $"))
    try:
        if bet > balance:
            print("Insufficient funds!!.")
            checkBet()
        elif bet <=0:
            print("Invalid bet amount.")
            checkBet()
    except ValueError:
            print("Invalid input. Please enter a valid number.")
            checkBet()
symbols = ['⭐️', '🍒', '🍋', '🍉', '🍇']
slot = []
balance = 100
bet =""
print("Welcome to the Slot Machine!")
print(f"Your balance is: ${balance}")
print("----- Place a bet -----")

while True:
  print("-----------------------\n")
  checkBet()
  if balance == 0:
    print("Game over.")
    break
  else:
    balance -= bet
    spin()
    print("\n",reward())
    print(f"````Current balance: ${balance}````")
    keepPlaying = input("Another bet? (Y,N): ").upper()
    if keepPlaying == 'Y':
      continue
    elif keepPlaying == 'N':
      print("Thanks for playing!!")
      break
    else:
      print("Invalid response. Exiting Game...")
      break
