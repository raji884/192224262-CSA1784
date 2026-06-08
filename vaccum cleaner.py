location = "A"          
room_A = "Dirty"
room_B = "Dirty"

print("Initial State:")
print("Room A =", room_A)
print("Room B =", room_B)
print()

while True:

    if location == "A":
        if room_A == "Dirty":
            print("Vacuum is in Room A")
            print("Cleaning Room A...")
            room_A = "Clean"
        location = "B"

    elif location == "B":
        if room_B == "Dirty":
            print("Vacuum is in Room B")
            print("Cleaning Room B...")
            room_B = "Clean"
        location = "A"

    if room_A == "Clean" and room_B == "Clean":
        break

print("\nGoal State Reached!")
print("Room A =", room_A)
print("Room B =", room_B)
