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

      
def main():
    """
    Main function to gather user's fitness profile.
    """
    user_level = set_user_level()

    print("\nUser Profile:")
    print(f"Level: {user_level.capitalize()}")


if __name__ == "__main__":
    main()
