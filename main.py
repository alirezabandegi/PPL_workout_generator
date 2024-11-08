import json
import random

def print_workout_structure():
    """Prints the structure of the Push-Pull-Legs (PPL) workout program."""
    structure = (
        "Workout Structure: The PPL program is split into three types of workouts:\n"
        "\t1. Push (P): Focuses on pushing muscles (chest, shoulders, and triceps).\n"
        "\t2. Pull (P): Focuses on pulling muscles (back and biceps).\n"
        "\t3. Legs (L): Focuses on lower body muscles (quadriceps, hamstrings, glutes, and calves).\n"
    )
    print(structure)


def print_weekly_rotation():
    """Prints the weekly rotation plan for a 4-day PPL program."""
    rotation = (
        "Weekly Rotation: Since you’re training four days a week, the workout days rotate each week "
        "to ensure balanced muscle engagement over time:\n"
        "\t- Week 1: P-P-L-P (Push, Pull, Legs, Push)\n"
        "\t- Week 2: P-L-P-P (Push, Legs, Pull, Push)\n"
        "\t- Week 3: L-P-P-P (Legs, Push, Pull, Push)\n"
        "This rotation ensures balanced development and muscle recovery over time."
    )
    print(rotation)


def print_workout_guide():
    """Prints the full workout guide for the PPL program."""
    print("PPL Workout Guide:")
    print("=" * 20)
    print_workout_structure()
    print()
    print_weekly_rotation()
    print("=" * 20)
    print("Note: Follow the rotation each week for balanced training and optimal muscle recovery.")


def load_exercises(file_path="exercises.json"):
    """Loads exercises from a JSON file and returns a list of exercises.
    
    Args:
        file_path (str): Path to the JSON file containing exercise data.
        
    Returns:
        list: List of exercise dictionaries.
    """
    with open(file_path) as f:
        return json.load(f)


def filter_exercises(exercises, level, goal, equipment):
    """Filters exercises based on user level, goal, and available equipment.
    
    Args:
        exercises (list): List of exercise dictionaries.
        level (str): User's experience level (e.g., "beginner", "intermediate", "advanced").
        goal (str): User's workout goal (e.g., "muscle gain").
        equipment (list): List of available equipment types.
        
    Returns:
        list: Filtered list of exercises matching user criteria.
    """
    return [
        exercise for exercise in exercises
        if exercise["intensity"].lower() == level.lower()
        and goal.lower() in map(str.lower, exercise["goal"])
        and any(eq in exercise["equipment"].lower() for eq in equipment)
    ]


def generate_workout_plan(ppl_split, target_sets_multiplier, filtered_exercises):
    """Generates a workout plan based on muscle groups and target sets.
    
    Args:
        ppl_split (dict): Dictionary defining muscle groups and base target sets.
        target_sets_multiplier (float): Multiplier for base target sets, based on workout duration.
        filtered_exercises (list): List of exercises filtered by user preferences.
        
    Returns:
        dict: Structured workout plan with exercises assigned to each muscle group.
    """
    workout_plan = {"Push": [], "Pull": [], "Legs": []}
    
    # For each workout type (Push, Pull, Legs), assign exercises
    for day_type, muscle_groups in ppl_split.items():
        for muscle, base_target_sets in muscle_groups.items():
            target_sets = int(base_target_sets * target_sets_multiplier)
            exercises_for_muscle = [
                exercise for exercise in filtered_exercises
                if any(muscle.lower() == m['muscle'].lower() for m in exercise['muscle_target'])
            ]
            
            selected_exercises = []
            sets_count = 0
            
            # Randomly assign exercises until target sets are met
            while exercises_for_muscle and sets_count < target_sets:
                exercise = random.choice(exercises_for_muscle)
                exercises_for_muscle.remove(exercise)
                
                sets = min(target_sets - sets_count, random.randint(2, 4))
                sets_count += sets
                selected_exercises.append((exercise["name"], sets))
            
            workout_plan[day_type].append((muscle, selected_exercises))
    
    return workout_plan


def display_final_workout_plan(final_plan, ppl_split, target_sets_multiplier):
    """Displays the final generated workout plan in a readable format.
    
    Args:
        final_plan (list): List of daily workout plans for the user.
        ppl_split (dict): Muscle groups and base target sets for each workout type.
        target_sets_multiplier (float): Multiplier for base target sets, based on workout duration.
    """
    print("\n\tPPL Program - Customized Workout")
    for day in final_plan:
        print(f"\n{day['day_type']} Day:")
        for muscle, exercises in day["muscles"]:
            print(f"{muscle} ({int(ppl_split[day['day_type']][muscle] * target_sets_multiplier)} sets)")
            for exercise, sets in exercises:
                print(f"  - {exercise} – {sets} sets")
        print("____________________________________\n")


def generate_workout(level, goal, equipment, duration, workout_days):
    """Generates and displays a PPL workout plan based on user preferences.
    
    Args:
        level (str): User's experience level.
        goal (str): User's workout goal.
        equipment (list): Available equipment types.
        duration (int): Duration of each workout session.
        workout_days (int): Number of workout days per week.
    """
    exercises = load_exercises()
    
    # Define the PPL split with base target sets per muscle group
    ppl_split = {
        "Push": {"Chest": 9, "Shoulders": 12, "Triceps": 9},
        "Pull": {"Back": 12, "Biceps": 9, "Traps": 6, "Abs": 6},
        "Legs": {"Quads": 12, "Hamstrings": 9, "Calves": 8}
    }
    
    # Set target sets multiplier based on workout duration
    duration_multipliers = {30: 0.5, 60: 1, 90: 1.5}
    target_sets_multiplier = duration_multipliers.get(duration, 1)
    
    # Filter exercises based on user preferences
    filtered_exercises = filter_exercises(exercises, level, goal, equipment)
    
    # Generate the workout plan
    workout_plan = generate_workout_plan(ppl_split, target_sets_multiplier, filtered_exercises)
    
    # Arrange workout days in a Push-Pull-Legs sequence
    day_names = ["Push", "Pull", "Legs"]
    final_plan = [
        {"day_type": day_names[i % 3], "muscles": workout_plan[day_names[i % 3]]}
        for i in range(workout_days)
    ]
    
    # Display the final workout plan
    display_final_workout_plan(final_plan, ppl_split, target_sets_multiplier)
    print_workout_guide()

# User setup functions (as defined previously)
def set_user_level():
    valid_levels = {'beginner', 'intermediate', 'advanced'}
    prompt = "Would you consider yourself a Beginner, Intermediate, or Advanced? "
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_levels:
            return user_input
        print("Invalid input. Please choose one of the following options: Beginner, Intermediate, or Advanced.")

def set_user_goal():
    valid_goals = {"muscle gain", "endurance", "strength building", "weight loss"}
    prompt = "What is your goal? (Muscle Gain, Endurance, Strength Building, Weight Loss): "
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_goals:
            return user_input
        print("Invalid input. Choose from Muscle Gain, Endurance, Strength Building, or Weight Loss.")

def set_user_equipment():
    equipment_list = ["Dumbbells", "Machine", "Cable", "Barbell", "Kettlebell"]
    available_equipment = ["bodyweight"]
    for equipment in equipment_list:
        while True:
            user_input = input(f"Do you have access to {equipment}? (y/n): ").strip().lower()
            if user_input in {'y', 'n'}:
                if user_input == 'y':
                    available_equipment.append(equipment.lower())
                break
            print("Invalid input. Please answer with 'y' or 'n'.")
    return available_equipment

def set_workout_duration():
    prompt = "How long would you like your workout to be? (30, 60, or 90 minutes): "
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in {30, 60, 90}:
                return user_input
            print("Invalid input. Please enter a number: 30, 60, or 90.")
        except ValueError:
            print("Invalid input. Please enter a valid integer: 30, 60, or 90.")

def set_preferred_workout_days():
    prompt = "How many days each week would you ideally like to work out? (3 to 6 days): "
    while True:
        try:
            user_input = int(input(prompt))
            if 3 <= user_input <= 6:
                return user_input
            print("Invalid input. Please enter a number between 3 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer between 3 and 6.")

def main():
    """Main function to run the workout generation program."""
    user_level = set_user_level()
    user_goal = set_user_goal()
    user_equipment = set_user_equipment()
    workout_duration = set_workout_duration()
    preferred_workout_days = set_preferred_workout_days()
    
    print("\nUser Profile:")
    print(f"Level: {user_level.capitalize()}")
    print(f"Goal: {user_goal.capitalize()}")
    print(f"Equipment: {', '.join(user_equipment) if user_equipment else 'None'}")
    print(f"Workout Duration: {workout_duration} minutes")
    print(f"Preferred Workout Days: {preferred_workout_days} days")

    generate_workout(user_level, user_goal, user_equipment, workout_duration, preferred_workout_days)

if __name__ == "__main__":
    main()