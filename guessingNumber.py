import random  # import random library

print("Guess the Number!")
# loop for condition if the player will keep playing or will playing
# this will break if it will exit
while True:
    # setting attempt to 7
    attempt = 7
    # getting random number to guess in from 1 to 100
    rand_num = random.randint(1, 100)
    # setting input_num to 0
    input_num = 0
    # count the number of attempt he make after he guess the random number
    count_attempt = 0
    # looping if number is not equal to the random number it will loop until it gets or the attempt is over
    while input_num != rand_num:
        # this will check if the attempt is greater than 0
        if attempt > 0:
            # storing the input in input_num
            input_num = int(input("Guess the number between 1 to 100: "))
            # condition for number if it is too high or too low for hint
            if input_num > rand_num:
                print("Too High. Try Again!")
                attempt -= 1
                count_attempt += 1
            # if the random number is guessed it will print message with number of attempts he made
            elif input_num == rand_num:
                print(
                    f"Congratulations! You have guess the number in {count_attempt} attempts!"
                )
            else:
                print("Too Low. Try Again!")
                attempt -= 1
                count_attempt += 1
        # if the attempt is equals 0 or over it will print sorry youve run out of guesses
        else:
            print(f"Sorry, you’ve run out of guesses!. The number was {rand_num}")
            break
        # condition if the player wants to continue the game
    cont = input(
        "Do you want to Continue the game?(Press any key and press 0 to exit): "
    )
    # if the input is equals 0 it will exit
    if cont == "0":
        break
