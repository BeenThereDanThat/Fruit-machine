
fruits = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

import random
credit = 1.00

def spin(credit):
  credit -= 0.2

  for fruit in range(0,3):
    fruitPicker = random.randrange(0,6)
    fruit1 = fruits[fruitPicker]
    fruitPicker = random.randrange(0,6)
    fruit2 = fruits[fruitPicker]
    fruitPicker = random.randrange(0,6)
    fruit3 = fruits[fruitPicker]
  roll = [fruit1,fruit2,fruit3]
  cherryCount = roll.count("Cherry")
  bellCount = roll.count("Bell")
  lemonCount = roll.count("Lemon")
  orangeCount = roll.count("Orange")
  starCount = roll.count("Star")
  skullCount = roll.count("Skull")
  print(roll)
  if cherryCount == 2 or bellCount == 2 or lemonCount == 2 or orangeCount == 2 or starCount == 2:
    print(" Congratulations you won 50p")
    credit += 0.50
    credit = round(credit, 1)
    print("Current Credit £"+ str(credit) + "0")
    again(credit)
  elif bellCount == 3:
    print("JACKPOT, you win £5")
    credit += 5.00
    credit = round(credit, 1)
    print("Current Credit £"+ str(credit) + "0")
    again(credit)

  elif cherryCount == 3  or lemonCount == 3 or orangeCount ==3 or starCount == 3:
    print(" Congratulations you won £1")
    credit += 1.00
    credit = round(credit, 1)
    print(f"Current Credit £" + str(credit) + "0")
    again(credit)
  elif skullCount == 3:

    print("Oh No, You lost it ALL")
    credit = 0.00
    credit = round(credit, 1)
    print("Current Credit £"+ str(credit) + "0")
    
  elif skullCount == 2:
    print("Oh No, You lost £1")
    credit -= 1.00
    credit = round(credit, 1)
    print("Current Credit £"+ str(credit) + "0")
    again(credit)
  else:
    print("Nothing this time")
    credit = round(credit, 1)
    print("Current Credit £"+ str(credit) + "0")
    again(credit)
  
  
def again(credit):
  print("""
╔═══╗───────╔╗───────────╔╗─╔╗
║╔═╗║───────║║───────────║║─║║
║╚═╝╠══╦╗╔╦═╝╠══╦══╦══╦╗╔╣╚═╣║╔══╗
║╔══╣══╣║║║╔╗║╔╗║╔╗║╔╗║╚╝║╔╗║║║║═╣
║║──╠══║╚╝║╚╝║╚╝║╚╝║╔╗║║║║╚╝║╚╣║═╣
╚╝──╚══╩══╩══╩══╩═╗╠╝╚╩╩╩╩══╩═╩══╝
────────────────╔═╝║
────────────────╚══╝
   """)
  Spin = input("\nWould you like to spin? \n(Y/N)\n").upper()
  if Spin == "Y" and credit <= 0.00:
    print("Please insert another credit to play\n\n")
    moreCredit = input("Would you like to insert another credit and continue playing?\n(Y/N)")

    if moreCredit == "Y":
        credit += 1.00
        spin(credit)

    else:
      print("OK, your cashout amount is £"+ str(credit) + "0")

  elif Spin == "Y":
  
    spin(credit)
  else:
    print("OK, your cashout amount is £"+ str(credit) + "0")
again(credit)
print("somestuff")