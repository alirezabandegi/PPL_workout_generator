# PPL Workout Generator

This repository contains a Python-based Push-Pull-Legs (PPL) workout generator that customizes workout plans based on user-defined preferences. This program supports users of all fitness levels and goals, offering personalized routines based on workout duration, available equipment, and preferred muscle focus.

## Features

- **Customizable PPL Plans**: Generates tailored workout routines for "Push," "Pull," and "Legs" days, supporting balanced development across major muscle groups.
- **Personalized Filters**: Filters exercises by intensity level, workout goals, and equipment availability.
- **Flexible Workout Durations**: Adjusts target sets and exercise counts based on user-selected workout duration (30, 60, or 90 minutes).
- **User-Friendly Structure**: Outputs workout plans in a clear, easy-to-read format, along with a workout guide and weekly rotation schedule.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Example Output](#example-output)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alirezabandegi/PPL_workout_generator.git
   cd PPL_workout_generator
   ```

2. Ensure you have **Python 3.12.7** installed. This script uses no additional packages beyond the Python standard library.

## Usage

1. The repository contains a Python script (`main.py`) and a JSON file (`exercises.json`) with predefined exercises. The `exercises.json` file contains detailed information about each exercise, including its target muscles, intensity, goal, and required equipment. Ensure the `exercises.json` file is in the same directory as the script.

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the interactive prompts to select your workout preferences. These include experience level, goals, available equipment, workout duration, and preferred workout days per week.

### Example Input

- **Level**: Beginner, Intermediate, or Advanced
- **Goal**: Muscle gain, fat loss, endurance, etc.
- **Equipment**: Available equipment, e.g., barbell, dumbbells, or bodyweight
- **Workout Duration**: 30, 60, or 90 minutes
- **Days per Week**: Number of days you plan to work out

## Configuration Options

| Option          | Description                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| Level           | Specifies experience level (beginner, intermediate, advanced).                                |
| Goal            | Determines primary workout focus (e.g., muscle gain, fat loss, endurance).                    |
| Equipment       | List of available equipment; the program selects compatible exercises.                        |
| Duration        | Workout duration (30, 60, or 90 minutes) scales exercise sets accordingly.                    |
| Days per Week   | Number of days for PPL sessions; adjusts routine to balance muscle engagement each week.      |

## Example Output

Upon completing the prompts, the program displays a weekly workout plan and a PPL guide, such as:

```
Would you consider yourself a Beginner, Intermediate, or Advanced? Beginner
What is your goal? (Muscle Gain, Endurance, Strength Building, Weight Loss): Muscle Gain
Do you have access to Dumbbells? (y/n): y
Do you have access to Machine? (y/n): y
Do you have access to Cable? (y/n): y
Do you have access to Barbell? (y/n): y
Do you have access to Kettlebell? (y/n): y
How long would you like your workout to be? (30, 60, or 90 minutes): 30
How many days each week would you ideally like to work out? (3 to 6 days): 3

User Profile:
Level: Beginner
Goal: Muscle gain
Equipment: bodyweight, dumbbells, machine, cable, barbell, kettlebell
Workout Duration: 30 minutes
Preferred Workout Days: 3 days

        PPL Program - Customized Workout

Push Day:
Chest (4 sets)
  - Chest Fly (Dumbbells) – 2 sets
  - Beginner Chest Fly – 2 sets
Shoulders (6 sets)
  - Shoulder Press Machine – 3 sets
  - Beginner Shoulder Press – 2 sets
  - Shoulders Squat – 1 sets
Triceps (4 sets)
  - Beginner Tricep Kickback – 4 sets
____________________________________


Pull Day:
Back (6 sets)
  - Biceps Extension – 2 sets
  - Seated Row (Machine) – 2 sets
  - Lat Pulldown Machine – 2 sets
Biceps (4 sets)
  - Bicep Curl (Dumbbell) – 4 sets
Traps (3 sets)
  - Single Arm Kettlebell Shrug – 2 sets
  - Dumbbell Upright Row – 1 sets
Abs (3 sets)
  - Leg Raises – 3 sets
____________________________________


Legs Day:
Quads (6 sets)
  - Leg Press (Machine) – 4 sets
  - Step-Ups (Bodyweight) – 2 sets
Hamstrings (4 sets)
  - Single-Leg Romanian Deadlift (Dumbbell) – 4 sets
Calves (4 sets)
  - Standing Calf Raises – 2 sets
  - Quads Squat – 2 sets
____________________________________

PPL Workout Guide:
====================
Workout Structure: The PPL program is split into three types of workouts:
        1. Push (P): Focuses on pushing muscles (chest, shoulders, and triceps).
        2. Pull (P): Focuses on pulling muscles (back and biceps).
        3. Legs (L): Focuses on lower body muscles (quadriceps, hamstrings, glutes, and calves).


Weekly Rotation: the workout days rotate each week to ensure balanced muscle engagement over time:
        - Week 1: P-P-L-P (Push, Pull, Legs, Push)
        - Week 2: P-L-P-P (Push, Legs, Pull, Push)
        - Week 3: L-P-P-P (Legs, Push, Pull, Push)
          Continue this rotation each week.
This rotation ensures balanced development and muscle recovery over time.
====================
Note: Follow the rotation each week for balanced training and optimal muscle recovery.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy training! If you encounter any issues, feel free to open an issue or contribute to this project.
