phone_mins = [
    [341, 74, 442, 185, 521],  # Kobe
    [256, 489, 98, 403, 132],  # Clyne
    [388, 211, 554, 167, 315]   # Psalm
]

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
most_active = ""
max_total = 0

# Loop through each day (column index 0 to 4)
for d in range(5):
    day_total = 0
    # Add up every person's minutes for this specific day
    for person_row in phone_mins:
        day_total += person_row[d]
    print(f"Total for {days[d]}: {day_total}")
    if day_total > max_total:
        max_total = day_total
        most_active = days[d]
print(f"The most active day overall was {most_active} with {max_total} mins.")
