date = input("Enter today's date: ")
mood = input("How do you rate your mood from 1 do 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../journal_bonus8/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)