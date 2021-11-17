print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice = ""
choice = input("""You're at cross road. Where do you want to go? Type \"left\" or \"right\"\n""").lower()

if choice == "left":
  choice = input("""You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n""").lower()
  if (choice == "swim"):
    print("""A crocodile attacked you, you\'re dead. GAME OVER!!""")
  elif choice == "wait":
    choice = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n""").lower()
    if choice == "red":
      print("You got burned by fire. GAME OVER!!!")
    elif choice == "blue":
      print("You got eaten by a beast. GAME OVER!!!")
    elif choice == "yellow":
      print("YOU FOUND THE TREASURE, YOU WIN!!!")
    else:
      print("""You have to type either \"red\", \"yellow\" or \"blue\", any other word doesn't work!""")
  else:
    print("""You have to type either \"swim\" or \"wait\", any other word doesn't work!""")
elif choice == "right":
  print("""You just fell into a Hole. GAME OVER!!!""")
else:
  print("""You have to type either \"left\" or \"right\", any other word doesn't work!""")