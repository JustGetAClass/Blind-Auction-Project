from replit import clear
from art import logo

bidders = {}
end_bid = True

def highest_bidder(bidders):
  highest = 0
  for key in bidders:
    if bidders[key] > highest:
      highest = bidders[key]
      winner = key
  print(f"The winner is {winner} with ${highest}")
  
while end_bid:
  print(logo)
  
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
   
  bidders[name] = bid
  
  cont = input("continue? yes or no")
  if cont == "no":
    end_bid = False
    print(bidders)
    highest_bidder(bidders)
  elif cont == "yes":
    clear()
  
 