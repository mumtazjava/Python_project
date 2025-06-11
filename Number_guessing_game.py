import random  # 🎲 Importing random module to generate a random number

# 👋 Welcome Message
print("🎉 Welcome to the Guessing Game!")

# ✅ Ask the user if they want to play
playing = input("🤔 Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    print("👋 Okay, maybe next time!")
    quit()  # ❌ Exit the game if user says no

# 🎯 Ask user to enter the upper limit for the random number
top_of_range = input("🔢 Enter the upper limit of your guessing range: ")

# ✅ Check if user input is a number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("⚠️ Please enter a number greater than ZERO next time.")
        quit()
else:
    print("❌ Please enter a valid number next time.")
    quit()

# 🎲 Generate a random number between 0 and top_of_range
random_number = random.randint(0, top_of_range)
attempt = 0  # 🧮 To count the number of attempts

# 🔁 Start the guessing loop
while True:
    attempt += 1  # ➕ Increase attempt count with each guess
    user_guess = input("🎯 Enter your guessed number: ")

    # ✅ Check if the guess is a number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("❌ Please type a valid number next time.")
        quit()

    # 🎯 Check if the guess is correct
    if user_guess == random_number:
        print(f"🎉 Congratulations! You guessed it right in {attempt} attempt(s) 🎯")
        break  # 🛑 Exit the loop when guessed correctly
    elif user_guess > random_number:
        print("📈 Too high! Try again ⬇️")
    else:
        print("📉 Too low! Try again ⬆️")
