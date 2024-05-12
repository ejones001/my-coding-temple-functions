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

# Example usage:
activity = 'Dancing'
duration = 10

calories_burned = estimate_calories_burned(activity, duration)
print(f"Estimated calories burned for {activity} for {duration} minutes: {calories_burned}")


# Example usage:
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
