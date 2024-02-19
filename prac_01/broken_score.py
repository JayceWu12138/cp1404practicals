MINIMUM_LIMIT = 0
MAXIMUM_LIMIT = 100
HIGH_THRESHOLD = 90
LOW_THRESHOLD = 50
score = float(input("Enter score: "))
if score < MINIMUM_LIMIT or score > MAXIMUM_LIMIT:
    print("Invalid score")
elif score >= HIGH_THRESHOLD:
    print("Excellent")
elif score >= LOW_THRESHOLD:
    print("Passable")
else:
    print("Bad")
