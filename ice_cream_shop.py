"""
Customer is welcomed to Ice Cream Town. They are then placed into an Ordering-While-Loop, 
asking for cup/cone, number of scoops between 1-3, and then which flavors they'd like.
Their order it repeated back to them, and then prompted if they'd like to place another order. 
If the answer is no, they are wished a good day and the loop ends. If they want more, 
the entire Ordering-While-Loop until they break the loop with saying they're done ordering.
"""


# Initialized variables
flavors = (
    "chocolate",
    "vanilla",
    "strawberry",
    "mint",
    "caramel",
    "oreo"
)

print("Welcome to Ice Cream Town!")

while True:

    # Initialized variable
    chosen_flavors = []

    # Choose Container
    while True:
        vessel = input("Would you like a cone or cup? ").lower()
        if vessel in ["cup", "cone"]:
            break
        else: 
            print("Please choose a cup or a cone.")

    # Choose Scoops
    while True:
        scoops = input("Would you like 1, 2, or 3 scoops? ")
        if scoops.isdigit():
            scoops = int(scoops)
            if 1 <= scoops <= 3:
                break   
        else:
            print("Please choose between 1, 2, or 3 ")

    # Choose Flavors
    for i in range(scoops):
        while True:
            flavor = input(f"Choose flavor for scoop {i + 1} from {', '.join(flavors)}: ")
            if flavor in flavors: 
                chosen_flavors.append(flavor)
                break
            else:
                print(f"Please choose from the avilable flavors: {', '.join(flavors)}.")

    # Confirm order
    print(f"You ordered a {vessel} with {scoops} scoops of {', '.join(chosen_flavors)}.")

    # Continue or stop ordering
    while True:
            more_order = input("Would you like to order anything else? (yes or no) ").lower()
            if more_order in ["yes", "no"]:
                break 
            else:
                print("Please answer 'yes' or 'no'.")
        
    if more_order == "no":
        break 
                

print("Thank you for your order and have a great day!")

