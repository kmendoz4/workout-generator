import random

print("Welcome to my workout generator!")

print("First, choose the type of workout you want:")
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
    "Tricep Extension 2x10-12",
    "Lateral Raise 2x10-12",]

if type == 1:
    print(random.choice(upper_chest_compound))
    print(random.choice(upper_shoulder_compound))
    print(random.choice(upper_back_compound))
    print(random.choice(upper_lat_compound))
    print(random.choice(upper_accessory))
    print(random.choice(upper_accessory))

