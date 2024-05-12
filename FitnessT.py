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

# Example usage:
activities = ["Dancing", "Swimming", "Biking", "Running","Wall Climbing"]
durations = [10, 20, 15,30,25]

fitness_log = log_fitness_activities(activities, durations)
print(fitness_log)
