import os

# Define the range of days
start_day = 5
end_day = 100

# Create files for each day
for day in range(start_day, end_day + 1):
    filename = f"day-{day}.py"
    if not os.path.exists(filename):  # Avoid overwriting existing files
        with open(filename, 'w') as file:
            file.write(f"# Day {day} Python Script\n")
        print(f"Created: {filename}")
    else:
        print(f"Skipped (already exists): {filename}")
