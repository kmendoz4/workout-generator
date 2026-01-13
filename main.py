import random

workouts = {
    "squat" : {
        "squat_variations" : ["Back Squat 3x8", "Front Squat 3x8"],
        "back" : ["Lat Pulldown 2x10-12 to Drop Set", "Pull-Ups 3x10-12", "Face Pulls 3x12\nBack Extensions 3x10",
                  "Normal Grip Lat Pulldown 2x10-12\nWide Grip Lat Pulldown 2x10-12"],
        "shoulder" : ["DB Shoulder Press 3x10\nRear Delt Flies 3x15", "BB Shoulder Press 3x10\nFront Raises3x12", "Cuban Press 4xAMRAP"],
        "arms" : ["Alternating Curls 2x6-8 to Drop Set\nSingle Arm Tricep Pulldowns 3x12", "Single DB Curls Superset with Overhead Tricep Extensions 3x12"]
    },
    "press" : {
        "press_variations" : ["BB Bench Press 3x8", "DB Bench Press 3x8", "DB Incline Press 3x8"],
        "legs" : ["BB Hip Thrust 3x8-10", "Hip Abduction 3x10\nHip Adduction 3x10", "RDLs 3x12", "Heel Elevated Goblet Squat 3x12"],
        "shoulder" : ["DB Lat Raise Superset Rear Delt Flies 3xAMRAP", "Farmers Carry 3 sets"],
        "arms" : ["Preacher Curl 3x12\nWrist Curls 3x12", "Zottman Curls 3x12\nTricep Pushdowns 3x12"]
    },
    "deadlift" : {
        "deadlift_variation" : ["Deadlift 3x5", "Deadlift 3x8"],
        "chest" : ["Decline Push-Ups 3xAMRAP", "Chest Flies 3x10"],
        "back" : ["DB Single Arm Row 3x10", "Seated Row 3x10", "Face Pulls 3x12\nStraight Arm Pulldowns 3x12"],
        "legs" : ["Leg Extensions 3x10\nHamstring Curl 3x10\nCalf Raises 3x12"]
    }
}

def generate_workout(workout_type):
    random_workout = []
    exercise_list = workouts[workout_type].values()

    for exercises in exercise_list:
        random_workout.append(random.choice(exercises))
    
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
elif type == 2:
    print("\n".join(generate_workout("press")))
elif type == 3:
    print("\n".join(generate_workout("deadlift")))
print("\n")