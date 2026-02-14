import random

# Main compound lifts for each day
main_lifts = {
    "squat": ["Back Squat", "Front Squat", "Safety Bar Squat", "Pause Squat"],
    "push/pull": ["Bench Press", "Incline Bench Press", "Overhead Press", "Close-Grip Bench Press"],
    "deadlift": ["Conventional Deadlift", "Sumo Deadlift", "Trap Bar Deadlift", "Deficit Deadlift"]
}

# Secondary lifts and accessories
workouts = {
    "squat": {
        "secondary_lift": ["Bulgarian Split Squat", "Leg Press", "Heel-Elevated Goblet Squat"],
        "accessories": ["Leg Extensions", "Sissy Squats", "Hip Thrusts", "Cable Kickbacks", 
                       "Abductor Machine", "Calf Raise", "Step-Ups (Quad Focused)", 
                       "Adductor Machine", "Copenhagen Planks", "Hanging Leg Raises", "Cable Crunches"]
    },
    "push/pull": {
        "accessories": ["DB Lateral Raises", "Cable Lateral Raises", "Upright Cable Raises (light)",
                       "Pec Deck", "Incline Cable Flyes", "Single-Arm Cable Rows", 
                       "Straight-Arm Pulldowns", "Face Pulls", "EZ-Bar Curls", 
                       "Incline DB Curls", "Rope Tricep Pushdowns", "Overhead Tricep Extensions"]
    },
    "deadlift": {
        "secondary_lift": ["Hip Thrust", "Barbell Good Morning", "Deficit RDL"],
        "accessories": ["Seated Hamstring Curl", "Nordic Curl", "Cable Pull-Throughs", 
                       "Reverse Lunges", "Smith Machine Lunges", "Back Extensions", 
                       "EZ Bar Curls", "DB Curls", "Tricep Pushdowns"]
    }
}

def generate_workout(workout_type, accessories_count):
    random_workout = []
    
    # 1. Pick a main compound lift
    main_lift = random.choice(main_lifts[workout_type])
    random_workout.append(f"MAIN LIFT: {main_lift}")
    
    # 2. Pick 1 secondary lift (if available)
    if "secondary_lift" in workouts[workout_type]:
        secondary = random.choice(workouts[workout_type]["secondary_lift"])
        random_workout.append(f"SECONDARY: {secondary}")
    
    # 3. Pick accessories based on user's count
    if "accessories" in workouts[workout_type]:
        accessories = workouts[workout_type]["accessories"]
        num_to_pick = min(accessories_count, len(accessories))
        selected_accessories = random.sample(accessories, k=num_to_pick)
        
        random_workout.append("\nACCESSORIES:")
        random_workout.extend(selected_accessories)
    
    return random_workout

print("=" * 50)
print("Welcome to my workout generator!")
print("=" * 50)

print("\n1. Generate Squat Day Workout")
print("2. Generate Push/Pull Workout")
print("3. Generate Deadlift Day Workout")

workout_type = int(input("\nEnter the number of your choice: "))
accessories = int(input("Enter the number of accessories for this workout: "))

print("\n" + "=" * 50)
print("YOUR WORKOUT:")
print("=" * 50 + "\n")

if workout_type == 1:
    print("\n".join(generate_workout("squat", accessories)))
elif workout_type == 2:
    print("\n".join(generate_workout("push/pull", accessories)))
else workout_type == 3:
    print("\n".join(generate_workout("deadlift", accessories)))

print("\n" + "=" * 50)