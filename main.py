import random

workouts = {
    "squat" : {
        "secondary_lift" : ["Bulgarian Split Squat", "Leg Press", "Heel-Elevated Goblet Squat"],
        "accessories" : ["Leg Extensions", "Sissy Squats", "Hip Thrusts", "Cable Kickbacks", "Abductor Machine", "Calf Raise", "Step-Ups(Quad Focused)", "Adductor Machine", "Copenhagen Planks", "Hanging Leg Raises", "Cable Crunches"]
    },
    "push/pull" : {
        "shoulders" : ["DB Lateral Raises", "Cable Lateral Raises", "Upright Cable Raises (light)"],
        "chest" : ["Pec Deck", "Incline Cable Flyes"],
        "back" : ["Single-Arm Cable Rows", "Straight-Arm Pulldowns", "Face Pulls"],
        "arms" : ["EZ-Bar Curls", "Incline DB Curls", "Rope Tricep Pushdowns", "Overhead Tricep Extenstions"]
    },
    "deadlift" : {
        "secondary_lift" : ["Hip Thrust", "Barbell Good Morning", "Deficit RDL"],
        "accessories" : ["Seated Hamstring Curl", "Nordic Curl", "Cable Pull-Throughs", "Reverse Lunges", "Smith Machine Lunges", "Back Extensions", "EZ Bar Curls", "DB Curls", "Tricep Pushdowns"]
    }
}

# ideas - make push/pull into one accessories dictionary moment
# ask it to pick a day, then a main compound lift, then ask how many accessories they want
# the generator will have workout_type AND number of accessories as a parameter

def generate_workout(workout_type, accessories_count):
    random_workout = []

    for exercises in workouts[workout_type].values():
        # Pick the smaller of: accessories_count or number of available exercises
        num_to_pick = min(accessories_count, len(exercises))
        random_workout.extend(random.sample(exercises, k=num_to_pick))

    return random_workout

print("Welcome to my workout generator!")

print("\n1. Generate Squat Day Workout")
print("2. Generate Push/Pull Workout")
print("3. Generate Deadlift Day Workout")
print("4. Gemerate HIIT/SIT Day Workout")

type = int(input("Enter the number of your choice: "))
accessories = int(input("\nEnter the number of accessories for this workout"))
print("\nYour workout:\n")

if type == 1:
    print("\n".join(generate_workout("squat", accessories)))
elif type == 2:
    print("\nMain Push ")
    print("\n".join(generate_workout("press", accessories)))
elif type == 3:
    print("\n".join(generate_workout("deadlift", accessories)))
    print("\n")