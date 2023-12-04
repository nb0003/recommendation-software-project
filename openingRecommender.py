from openingData import opening_data
from recommendfunctions.functions import gameplay_dictionary, opening_dictionary, display_opening, type_dictionary

def get_user_choice(options, prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def main():
    # Organize openings
    organized_openings = opening_dictionary(opening_data)

    # Types and gameplay choices
    types = ['classic', 'unusual']
    gameplay = ['open', 'semi-open', 'closed', 'semi-closed']

    displayed_openings = set()  # To keep track of displayed openings

    while True:
        # User selects opening type
        type_choice = get_user_choice(types, "What opening type would you like to play? \nEnter option: ")

        # User selects gameplay type
        gameplay_choice = get_user_choice(gameplay, "What gameplay type are you looking to play? \nEnter option: ")

        # Confirm user choices
        type_confirmation = input(f"\nWould you like to view {type_choice} openings? \n y/n: ").strip().lower()
        gameplay_confirmation = input(f"Would you like to view {gameplay_choice} openings? \n y/n: ").strip().lower()

        # Display openings based on user choices
        if type_confirmation == 'y':
            print(f"The {type_choice} openings are: ", end="\n\n")
            if type_choice in organized_openings:
                type_dict = organized_openings[type_choice]
                if gameplay_choice in type_dict:
                    display_opening(type_dict[gameplay_choice])
                else:
                    print(f"No {gameplay_choice} openings found for {type_choice}.")
            else:
                print(f"No openings found for {type_choice}.")

        if gameplay_confirmation == 'y':
            print(f"The {gameplay_choice} openings are: ", end="\n\n")
            if gameplay_choice in organized_openings:
                gameplay_dict = organized_openings[gameplay_choice]
                if type_choice in gameplay_dict:
                    display_opening(gameplay_dict[type_choice])
                else:
                    print(f"No {type_choice} openings found for {gameplay_choice}.")
            else:
                print(f"No openings found for {gameplay_choice}.")


        # Ask if the user wants to continue
        continue_input = input("Would you like to continue? (y/n): ").strip().lower()
        if continue_input != 'y':
            print("Thanks for using opening recommender! Bye!")
            break


if __name__ == "__main__":
    print("""
       .__                                                       .__                
  ____ |  |__   ____   ______ ______   ____ ______   ____   ____ |__| ____    ____  
_/ ___\|  |  \_/ __ \ /  ___//  ___/  /  _ \\____ \_/ __ \ /    \|  |/    \  / ___\ 
\  \___|   Y  \  ___/ \___ \ \___ \  (  <_> )  |_> >  ___/|   |  \  |   |  \/ /_/  >
 \___  >___|  /\___  >____  >____  >  \____/|   __/ \___  >___|  /__|___|  /\___  / 
     \/     \/     \/     \/     \/         |__|        \/     \/        \//_____/  
                                                               .___                 
_______   ____   ____  ____   _____   _____   ____   ____    __| _/___________      
\_  __ \_/ __ \_/ ___\/  _ \ /     \ /     \_/ __ \ /    \  / __ |/ __ \_  __ \     
 |  | \/\  ___/\  \__(  <_> )  Y Y  \  Y Y  \  ___/|   |  \/ /_/ \  ___/|  | \/     
 |__|    \___  >\___  >____/|__|_|  /__|_|  /\___  >___|  /\____ |\___  >__|        
             \/     \/            \/      \/     \/     \/      \/    \/            
      """)

    main()
