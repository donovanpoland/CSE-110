

#creativity portion
"""
I had both my wife and my mother in law test my program, by letting them test it out I was able to find spelling, grammer and logic errors.
It was extreamly helpful as the logic was difficult to build and path each direction. 
I explained to them how programing is like using algibra with variables but even deeper that I can add logic to my code.
"""

#instructions to user
print("Welcome to Pathways Adventure Game, you will be presented with a story and options to choose from within the story.\n" + 
      "When you see a WORD in all caps like THIS, that will represent the OPTIONS you have, choose wisely.\n" +
      "Type in your prompted word and if you don't spell the word correctly you may find a surprise.\n")

#the story
print("You enjoy nature and decide one day to take a stroll through the woods but loose track of time and find your self in the dark.\n" +
      "Tonight, there is no moon, no stars and you're too far from civilization to see lights in the distance.\n" + 
      "You are in complete darkness. So you decide to dig through your backpack to find a flashlight but can't tell one item from another.\n")

#special conditions
home_path = "You slowly make it through the forest and back to civilization without any issues."
alt_home_path = ("You limp through the forest barely holding your flashlight, bleeding but alive.\n" + 
                 "Soon you see civilization and collapse from blood loss as someone finds you and gets you help.\nYour vision fades to darkness but you live.")
wolf = "You hear a growl and step backwards slowly. Something large slowly moves towards you."
eyes = "A set of eyes glare in your direction."
knife ="You open it and point it in the direction of the noise. "
death = ("A wolf jumps at you, bites your arms and drags you down to the ground, it then lunges at your neck and bites down hard, you can do nothing as the wolf tears out your throat.\n" + 
         "Your vision fades to black. You are dead." )
larger = "something larger chases after it. "
flashlight = "You dig one last time and find your flashlight and turn it on."
win_fight = "The wolf circles you and you watch it, it leeps forward biting your arm and with the other you stab it in the neck. You killed the alpha wolf and the other wolves run off."
alt_death = ("Your indecisiveness as you are running leads to the wolf jumping and biting at your legs, dragging you to the ground. Other wolves bite at your arms and they become useless.\n" +
             "Then an alpha wolf stares down at you in dominance and goes for the neck. Your vision fades to darkness.")
the_end = "The End."

#PATH 1
ridges = ("You pull something out but can't find a button to turn it on and you hear a rustling noise behind you.\n" + 
          "You realize that you had pulled a water bottle out of your backpack, do you turn and THROW it at the noise or stand STILL? ")
#path 1 fist set of choices
#choice THROW
throw = ("You turn and throw the water bottle at the sound, you hear rustling again but it seems to move away from you quickly.\n" + larger.capitalize() +
          "You dig in your backpack again and feel the same round ROUGH item from before and another METALLIC item.\n" + 
          "What one do you grab? ")
#choice STILL
still = ("You hold your breath and stand still, then you realize the sound starts to go in another direction and " + larger +
         "\nYou dig in your backpack again and feel the same round ROUGH item from before and another METALLIC item.\n" + 
          "What one do you grab? ")

#path 1 second set of choices
#choice ROUGH
alt_rough = "You manage to find your flashlight and turn it on."
#choice METALIC
metallic = "You manage to find your pocket knife and flip it open and close again."


#PATH 2
rough = flashlight + " You hear a rustling noise behind you, do you TURN towards the noise or RUN? "

#path 2 first set of choices
#choice RUN
run ="Flashlight in hand, you begin to run through the forest, something then begins to chase after you. Do you turn and FIGHT or RUN more? "
#choice TURN
turn = ("You point the flashlight at the noise and realize it is a rabbit. It runs off in a hurry, but " + eyes + 
        "\nDo you turn and FIGHT or RUN? ")

#path 2 second set of choices
#choice RUN
alt_run = ("As you are running a wolf jumps and bites at your legs, dragging you to the ground. You kick and fight back but the wolf is too strong.\n" + 
           "You can't reach your backpack anymore for something to help you fight. So you decide to reach up and squeeze the wolf's neck until it can't breath.\n" +
           "It fights you tooth and nail, but you succeed, barely.")

#choice FIGHT
fight = "You turn to face your foe, through quick thinking you dig in your backpack and grab your pocket knife."


#PATH 3
first_choise_alt = "You take too long to make a descison and become startled by a rustling noise behind you and drop your backpack and it hits the ground with a thud."




#first choise from user
first_choise = input("Do you grab the round item with RIDGES or the round item that is ROUGH to the touch? ")
#convert to lowercase for easy logic
first_choise = first_choise.lower()

#test
#print(first_choise)

#first choise logic
if first_choise == "ridges":
     #path 1 begin
     path1 = input(ridges)
     if path1.lower() == "throw":
          con_path1 = input(throw)
          if con_path1.lower() == "rough":
               print(f"{alt_rough} {home_path} {the_end}")
          elif con_path1.lower() == "metallic":
               print(f"{metallic} {flashlight} {home_path} {the_end}")
          else:
               print(f"{first_choise_alt} {eyes}\n{wolf}\n{death} {the_end}")
     elif path1.lower() == "still":
          con_path1 =input(still)
          if con_path1.lower() == "rough":
               print(f"{alt_rough} {home_path} {the_end}")
          elif con_path1.lower() == "metallic":
               print(f"{metallic}\n{flashlight} {home_path} {the_end}")
          else:
               print(f"{first_choise_alt} {eyes}\n{wolf}\n{death} {the_end}")
     else:
          print(f"{first_choise_alt} {eyes}\n{wolf}\n{death} {the_end}")
     #path 1 end
elif first_choise == "rough":
     #path 2 begin
     path2 = input(rough)
     if path2.lower() == "run":
          con_path2 = input(run)
          if con_path2.lower() == "fight":
               print(f"{fight}\n{knife}\n{win_fight}\n{alt_home_path} {the_end}")
          elif con_path2.lower() == "run":
               print(f"{alt_run} {the_end}")
          else:
               print(alt_death)
     elif path2.lower() == "turn":
          con_path2 = input(turn)
          if con_path2.lower() == "fight":
               print(f"{fight}\n{knife}\n{win_fight}\n{alt_home_path} {the_end}")
          elif con_path2.lower() == "run":
               print(f"{alt_run} {alt_home_path} {the_end}")
          else:
               print(alt_death)
     else:
          print(f"{first_choise_alt}\n{eyes} {wolf}\n{death} {the_end}")
     #path 2 end
else:
      #path 3
      print(f"{first_choise_alt} {eyes}\n{wolf}\n{death} {the_end}")

