import random

print("Welcome to my workout generator!")

print("Choose the type of workout you want:")
print("1. Upper Body")
print("2. Lower Body")
print("3. Full Body")
print("4. HIIT/SIT")

type = int(input("Enter the number of your choice: "))

upper_chest_compound = [
    "Barbell Bench Press 3x6-8",
    "Dumbbell Bench Press 3x6-8",
    "Dumbell Incline Press 3x6-8",
    "Deficit Push-Ups 3xfailure"]
    
upper_shoulder_compound = [
    "Overhead Press 3x6-8",
    "Dumbbell Shoulder Press 3x6-8",
    "Upright Barbell Row 3x6-8",]
    
upper_back_compound = [
    "Seated Row 3x6-8",
    "Barbell Row 3x6-8",]
    
upper_lat_compound = [
    "Lat Pulldowns 3x10-12",
    "Pull-ups 3xfailure"]
    
upper_accessory = [
    "Bicep Curls 2x10-12",
    "Lateral Raise 2x10-12",]

upper_isolation = [
    "Dips 2x10-12",
    "Tricep Extensions 2x10-12",]

upper_workout = [
    random.choice(upper_chest_compound),
    random.choice(upper_shoulder_compound),
    random.choice(upper_back_compound),
    random.choice(upper_lat_compound),
    random.choice(upper_accessory),
    random.choice(upper_isolation)]

lower_main_compound = [
    "Squats 3x8-10",
    "Deadlift 3x6-8"]

lower_secondary_compound = [
    "Lunges 3x8-10",
    "Single Leg Leg Press 3x8-10",
    "Hip Thrusts 3x8-10"]

lower_accessory = [
    "Leg Extension 3x8-10",
    "Calf Raise 3x12"]

lower_isolation = [
    "Hamstring Curl 3x8-10",
    "RDL 3x8-10"]

lower_workout = [
    random.choice(lower_main_compound),
    random.choice(lower_secondary_compound),
    random.choice(lower_accessory),
    random.choice(lower_isolation)]

if type == 1:
    print(*upper_workout, sep='\n')
elif type == 2:
    print(*lower_workout, sep='\n')