import time

# Example: Countdown timer
def countdown(seconds):
    print("Countdown starts!")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)  # Pauses for 1 second
    print("Time's up!")

# Example: Measure the time taken for a task
start_time = time.time()
countdown(5)  # Run countdown for 5 seconds
end_time = time.time()

# Calculate and display the elapsed time
elapsed_time = end_time - start_time
print("Total time taken:", elapsed_time, "seconds")
