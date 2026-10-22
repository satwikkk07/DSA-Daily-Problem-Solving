import random
n = random.randint(1,100)

a = 0
guesses = 1

while a != n:
    a = int(input("Enter your guess: "))
    guesses += 1

    if a<n:
        print("Higher number please!")
    elif a>n:
        print("Lower number please!")    

print(f"Congratulations! You guessed number {n} in {guesses} guesses.")