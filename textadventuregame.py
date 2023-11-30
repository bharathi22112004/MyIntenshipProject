import time

# Function to introduce the game
def introduction():
    print("Welcome to Space Adventure!")
    print("You wake up on a space station with no memory of how you got there.")
    print("Your mission is to explore space, make decisions, and find a way back home.\n")

# Function to present choices and get player's decision
def get_choice():
    print("What do you want to do?")
    print("1. Explore the space station")
    print("2. Investigate the nearby planet")
    print("3. Repair the damaged spaceship")
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Function for different outcomes based on choices
def explore_space_station():
    print("\nYou discover a hidden compartment with useful tools.")
    print("You fix some equipment and gain access to a secret passage.")
    time.sleep(2)
    print("Suddenly, an alarm goes off! The station is under attack.")
    time.sleep(2)
    print("You manage to escape through the secret passage and find an abandoned spaceship.")

def investigate_planet():
    print("\nYou land on the planet and encounter a friendly alien species.")
    print("They offer you advanced technology in exchange for your help.")
    time.sleep(2)
    print("You assist them in repairing their communication device.")
    time.sleep(2)
    print("They thank you and give you coordinates to a distant star system.")

def repair_spaceship():
    print("\nYou start repairing the spaceship's engine.")
    print("After hours of work, the engine is finally operational.")
    time.sleep(2)
    print("You blast off into space and head towards the unknown.")

def main():
    introduction()
    while True:
        choice = get_choice()

        if choice == '1':
            explore_space_station()
            break
        elif choice == '2':
            investigate_planet()
            break
        elif choice == '3':
            repair_spaceship()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if _name_ == "_main_":
    main()