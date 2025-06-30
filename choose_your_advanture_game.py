name =input("Type your name:")

print(f"Hey! {name} Welcome to this adventure")

answer=input("You are on a dirty road,it has to an end You can left or right which wey would you like to go?").lower()
if answer =='left':
  answer=input("You come to a river,you can walk🚶 around it or swim🏊 accross?type walk for walk arroun swim to swim accross").lower()
  if answer=='swim':
      print("You swim acrross and were eaten by a crocodile🐊")
      quit()
  elif answer=="walk":
      print("you walk many milles and run for a water and you lost ")
      
  else:
       print("Please Enter a vilade option")      
elif answer=='right':
     answer=input("You come to bridge, it looks wobbly, do you wnt to cross it or head back?type (cross/back) ").lower()
     if answer=='back':
      print("You go back and loss")
      quit()
     elif answer=="cross":
         answer=input("you cross the bridge and see a streange You want to tallk him or not type(talk/No)").lower()
         if answer=='talk':
            print("You talk to stanger and he give gold to you , You win!🏆")
            quit()
         elif answer=="no":
          print("you walk many milles and run for a water and you lost ")
      
         else:
          print("Please Enter a vilade option")     
      
     else:
       print("Please Enter a vilade option")     
    

else:
    print("Please Enter a vilade option")