# loops in python with user input
shopping_list = []
while True:
    item = input(
        "Enter an item to add to your shopping list (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)

    print("Your shopping list:", shopping_list)

# Ask the user how many inputs they want to add
num_items = int(input("How many scores do you want to add? "))
scores = []
for i in range(num_items):
    score = input(f"Enter score {i + 1}: ")
    scores.append(score)

print("All entered items:", scores)
print("Your average score:", sum(float(score)
      for score in scores) / len(scores))

while True:
    try:
        age = int(input("Please enter your age (as a number): "))
        if age < 0:
            print("Age cannot be negative. Try again.")
            continue  # Skips the rest of the loop and restarts it
        break  # Exits the loop if the input is a valid positive integer
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

print(f"Thank you. Your age is recorded as {age}.")
