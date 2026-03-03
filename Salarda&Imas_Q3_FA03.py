phone_mins = [
    [341, 74, 442, 185, 521],  # Kobe
    [256, 489, 98, 403, 132],  # Clyne
    [388, 211, 554, 167, 315]   # Psalm
]

names = ["Kobe", "Clyne", "Psalm"]
m1 = 0
for i in range(len(phone_mins)):
    row = phone_mins[i]
    name = names[i]
    total = sum(row)
    avg = total / len(row)
    rm = max(row)
    print(f"{name}'s Weekly Minutes: {row}")
    print(f"Total: {total} mins", f"Average: {avg} mins")
    if rm > m1:
        m1 = rm

print(f"Overall Maximum Usage in Dataset: {m1} mins")

