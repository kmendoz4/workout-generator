import random

class WorkoutTracker:
    def __init__ (self):
        self.workouts = { # workout dictionary
            "squat" : {
                "squat_variations" : ["Back Squat 3x6", "Front Squat 3x8-10", ""] #\n for enter
            }
        }

print("Welcome to my workout generator!")

print("\n1. Generate Squat Day Workout")
print("2. Generate Press Day Workout")
print("3. Generate Deadlift Day Workout")
print("4. Gemerate HIIT/SIT Day Workout")

type = int(input("Enter the number of your choice: "))