def main():
    truth = 666
    guess = int(input("Enter your guess: "))
    compare(truth, guess)

def compare(truth, guess):
    if truth == guess:
        print("Just right!")
    elif truth < guess:
        print("Too high!")
    else:
        print("Too low!")

main()