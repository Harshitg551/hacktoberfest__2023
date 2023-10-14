import random

def play_game():
    print("Welcome to the Higher or Lower Game!")

    score = 0
    prev_number = random.randint(1, 10)
    
    while True:
        print("Current number:", prev_number)
        user_guess = input("Will the next number be higher (h) or lower (l)? ").lower()

        if user_guess not in ['h', 'l']:
            print("Invalid input. Please enter 'h' for higher or 'l' for lower.")
            continue

        next_number = random.randint(1, 10)
        print("Next number:", next_number)

        if (next_number > prev_number and user_guess == 'h') or (next_number < prev_number and user_guess == 'l'):
            print("Correct guess!")
            score += 1
        else:
            print("Incorrect guess. Game over. Your score:", score)
            break

        prev_number = next_number

if __name__ == "__main__":
    play_game()
