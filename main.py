def set_user_level():
    """
    Prompts the user to select their experience level.
    Returns:
        str: User's experience level ('beginner', 'intermediate', 'advanced').
    """
    valid_levels = {'beginner', 'intermediate', 'advanced'}
    prompt = "Would you consider yourself a Beginner, Intermediate, or Advanced? "

    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_levels:
            return user_input
        print("Invalid input. Please choose one of the following options: Beginner, Intermediate, or Advanced.")

      
def set_user_goal():
    """
    Prompts the user to select their fitness goal.
    Returns:
        str: User's fitness goal ('muscle gain', 'endurance', 'strength building', 'weight loss').
    """
    valid_goals = {"muscle gain", "endurance", "strength building", "weight loss"}
    prompt = "What is your goal? (Muscle Gain, Endurance, Strength Building, Weight Loss): "

    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_goals:
            return user_input
        print("Invalid input. Choose from Muscle Gain, Endurance, Strength Building, or Weight Loss.")


def set_user_equipment():
    """
    Prompts the user for equipment availability.
    Returns:
        list: List of equipment the user has access to.
    """
    equipment_list = [
        "Dumbbells", "Machine", "Cable", "Barbell", "Kettlebell",
        "Treadmill", "Stationary Bike", "Jump Rope", "Rowing Machine", "Box",
        "Battle Rope", "Medicine Ball", "Agility Ladder", "Sled", "Rings",
        "Atlas Stone", "Pool", "Resistance Band"
    ]
    available_equipment = ["Bodyweight"]

    for equipment in equipment_list:
        while True:
            user_input = input(f"Do you have access to {equipment}? (y/n): ").strip().lower()
            if user_input in {'y', 'n'}:
                if user_input == 'y':
                    available_equipment.append(equipment)
                break
            print("Invalid input. Please answer with 'y' or 'n'.")

    return available_equipment


def main():
    """
    Main function to gather user's fitness profile.
    """
    user_level = set_user_level()
    user_goal = set_user_goal()
    user_equipment = set_user_equipment()

    print("\nUser Profile:")
    print(f"Level: {user_level.capitalize()}")
    print(f"Goal: {user_goal.capitalize()}")
    print(f"Equipment: {', '.join(user_equipment) if user_equipment else 'None'}")


if __name__ == "__main__":
    main()
