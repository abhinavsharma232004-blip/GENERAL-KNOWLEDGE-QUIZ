print("=" * 40)
print("      GENERAL KNOWLEDGE QUIZ")
print("=" * 40)

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
answer = input("3. How many continents are there? ").strip().lower()

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")








"bc mjaaa aa gya"

# Final Score
print("=" * 40)
print(f"Your final score is: {score}/3")
print("=" * 40)
