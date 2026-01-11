import random

workouts = {
    "squat" : {
        "squat_variations" : ["Back Squat 3x8", "Front Squat 3x8"],
        "back" : ["Lat Pulldown 2x10-12 to Drop Set", "Pull-Ups 3x10-12", "Face Pulls 3x12\nBack Extensions 3x10",
                  "Normal Grip Lat Pulldown 2x10-12\nWide Grip Lat Pulldown 2x10-12"],
        "shoulder" : ["DB Shoulder Press 3x10\nRear Delt Flies 3x15", "BB Shoulder Press 3x10\nFront Raises3x12", "Cuban Press 4xAMRAP"],
        "arms" : ["Alternating Curls 2x6-8 to Drop Set\nSingle Arm Tricep Pulldowns 3x12", "Single DB Curls Superset with Overhead Tricep Extensions 3x12"]
    }
}

def generate_workout(workout_type):
    random_workout = []
    exercise_list = workouts[workout_type].values()

    for exercises in exercise_list:
        chosen_exercise = random.choice(exercises)
        random_workout.append(chosen_exercise)
    
    return random_workout


print("Welcome to my workout generator!")

print("\n1. Generate Squat Day Workout")
print("2. Generate Press Day Workout")
print("3. Generate Deadlift Day Workout")
print("4. Gemerate HIIT/SIT Day Workout")

type = int(input("Enter the number of your choice: "))
print("\nYour workout:\n")

if type == 1:
    print("\n".join(generate_workout("squat")))

print("\n")