# 1. Nested Decisions: The Adventure Game 🏰

# Task 1: Code Correction
#You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.
# Buggy Code:
# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")
"""
The Bugs are:
1. Incorrect Assignment Operator,
2. Missing Indentation: 
"""
# Corrected Code:
# Use == for comparison
# For else: No need for assignment
place = input("Choose a place: forest or cave? ")
if place == "forest":  
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
elif place == "cave":  
    print("You find a hidden treasure!")


# Task 2: Setting the Scene
# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    torch_choice = input("Do you want to light a torch or proceed in the dark? ")
    if torch_choice.lower() == "light a torch":  
        print("You light your torch. You proceed cautiously.")
    elif torch_choice.lower() == "proceed in the dark":
        print("You feel you like to proceed in the dark. that's OK")


# Task 3: Default Path
# If the user makes an invalid choice at any point, use the pass statement for now. 
    else:
        pass  
else:
    pass  
