import random

""" using Lists and a randomizer and if statements to change elements of the story with more or less input from the user."""

# Default words if user chooses to randomize
adjectives = ["serene", "grumpy", "wild", "elegant", "peculiar", "cute", "mysterious", "frantic", "majestic", "grotesque",
               "vibrant", "mischievous", "bizarre", "sleek", "small", "gloomy", "prickly", "fluffy", "eerie"]

# different verbs for different parts of the story to  help with clearity
verbs1 = ["glide", "dance", "glow", "leap", "slide", "run", "bounce", "scurry","growl", "dig",]
verbs2 = ["whisper", "dance", "twitch", "whirl", "tremble",]
verbs3 = ["sprint", "charge", "pounce",  "sneak",] 


animals = ["penguin", "unicorn", "hamster", "dolphin", "dragon", "pigeon", "Koala","Chameleon", "Cheetah", "Octopus",
                 "hedgehog", "flamingo", "sloth", "gecko", "kangaroo", "lynx", "tortoise", "tarantula"]

exclamations = ["eureka", "wow", "oh no", "gadzooks", "holy moly", "hooray", "yikes", "bingo", "wowza!", "alas",]

# Additional random elements
locations = ["at the park", "in my house", "near the lake", "on Mars", "at the beach", "down the hallway"]

times = ["yesterday", "this morning", "last night", "a week ago", "five minutes ago"]

emotions = ["joyful.", "anxious.", "furious!", "curious!", "relieved.", "overwhelmed.", "content.", "frustrated!", "hopeful.",
             "excited!", "nervous.", "scared.", "confused!", "thrilled!"]

nouns = ["stop.", "explode!", "collapse.", "transform!", "disappear!"]

personages = ["my family", "my spouse", "my child", "my teacher", "a bunch of children", "a crowd", "my grandpa", "my grandma", "my cousin" ]

# collect user input for the story
print("\nCreate your own story.")

story_name = input("Please name your story: ")

print("\nPlease enter the following or type 'random' for a surprise: \n")

random_message = "Type 'r' for a random "
alt_r_mesg = "Type 'r' for another random "
manual_message = ' and then hit "enter" or continue to manual entry by pressing any key: '

location = random.choice(locations)

animal_type = input("Type of animal: ") if input(random_message + "type of animal" + manual_message) != 'r' else random.choice(animals)
# random time of day with no choise from the user to avoid poor sentance structures
time_of_day = random.choice(times)
exclamation = input("A word of exclamation!: ") if input(random_message + "word of exclamation" + manual_message) != 'r' else random.choice(exclamations)
emotion = input("An emotion: ") if input(random_message + "emotion" + manual_message) != 'r' else random.choice(emotions)
personage = input("A person or group: ") if input(random_message + "person or group" + manual_message) != 'r' else random.choice(personages)

adjective = input("Adjective: ") if input(random_message + "adjective" + manual_message) != 'r' else random.choice(adjectives)

verb1 = input("Verb: ") if input(random_message + "verb" + manual_message) != 'r' else random.choice(verbs1)
# asking for too much from user, removed a verb choise and made random only
verb2 = random.choice(verbs2)
verb3 = input("Verb: ") if input(alt_r_mesg + "verb" + manual_message) != 'r' else random.choice(verbs3)
# changing this noun becuase it makes the story more fun
noun = input("Noun: ") if input(random_message + "noun" + manual_message) != 'r' else random.choice(nouns)

# display story
print("\nYour story is: " + story_name + "\n")
print(f"{time_of_day.capitalize()}, I was feeling {emotion}")
# use single '' to use double "" inside paragraph
print(f'It all started when I saw a very {adjective} {animal_type} {verb1} {location}. {exclamation.capitalize()}!" I yelled.')
print(f"But all I could think to do was to {verb2} over and over.")
print(f"Miraculously, that caused it to {noun} But not before it tried to {verb3} right in front of {personage}.")