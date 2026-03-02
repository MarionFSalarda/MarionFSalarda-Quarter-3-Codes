phone_mins = [
    [341, 74, 442, 185, 521],  # Kobe
    [256, 489, 98, 403, 132],  # Clyne
    [388, 211, 554, 167, 315]   # Psalm
]

names = ["Kobe", "Clyne", "Psalm"]
top_name = ""
highest_total = 0
lowest_total = 10000  
for i in range(len(phone_mins)):
    row = phone_mins[i]
    name = names[i]
    total = sum(row)
    print(f"{name}'s Total: {total} mins")
    if total > highest_total:
        highest_total = total
        top_name = name
    if total < lowest_total:
        lowest_total = total
print(f"Top Performer: {top_name}")
print(f"Difference: {highest_total - lowest_total} mins")
