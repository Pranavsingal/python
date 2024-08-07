import random

guess = random.randint(1,10)

print(guess)

while True :
    number = int(input("gess the number ="))
    if (guess == number):
       print("you guesses correcrt no :)")
       print("___game-over-XD____")
       break
    elif(guess < number):
         print("chose something small")
    else:
         print("chose someting big")
   
