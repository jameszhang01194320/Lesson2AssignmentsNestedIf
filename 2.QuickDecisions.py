# 2. Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction
# Buggy Code:
# <="" code="" style="margin: 0px 0px 30px; padding: 0px; box-sizing: border-box; position: relative; display: block; min-height: 40px; width: 736.679px;">
# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)

# Corrected Code--change elif to else:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
vegetarian_choice = input("Would you like vegetarian food? (yes/no) ").lower()
food = "We recommend Veggie Delight Caterers" if vegetarian_choice == "yes" else "We recommend Gourmet Meals Caterers"
print(food)
