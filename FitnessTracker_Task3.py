def log_fitness_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: The number of activities must match the number of durations.")
        return
    
    log = {}
    for i in range(len(activities)):
        activity = activities[i]
        duration = durations[i]
        log[activity] = duration
    
    return log

def estimate_calories_burned(activity, duration):
    return duration * 3.5



activities = ["Dancing", "Swimming", "Biking", "Running","Wall Climbing"]
durations = [10, 20, 15,30,25]

# Log fitness activities
activity_log = log_fitness_activities(activities, durations)
print("Fitness Activity Log:")
for activity, duration in activity_log.items():
    print(f"- {activity}: {duration} minutes")

# Estimate calories burned for each activity
print("\nEstimated Calories Burned:")
for activity, duration in activity_log.items():
    calories_burned = estimate_calories_burned(activity, duration)
    print(f"- {activity}: {calories_burned} calories")

def generate_fitness_summary(activities, durations):
    # Log fitness activities
    activity_log = log_fitness_activities(activities, durations)
    
    # Initialize total calories burned
    total_calories_burned = 0
    
    # Print activity log
    print("\nFitness Activity Log:")
    for activity, duration in activity_log.items():
        print(f"- {activity}: {duration} minutes")
        # Estimate calories burned for each activity
        calories_burned = estimate_calories_burned(activity, duration)
        total_calories_burned += calories_burned
    
    # Print total calories burned
    print("\nTotal Calories Burned for the Day:", total_calories_burned, "calories")


generate_fitness_summary(activities, durations)

