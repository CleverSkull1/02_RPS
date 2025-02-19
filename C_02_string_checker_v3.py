def string_checker(question, valid_ans=('yes', 'no')):
    """Check that users have entered a valid option based on a list"""
    error = f"Please enter one of the following: " \
            f"{valid_ans}"

    while True:
        # get user response and make sure its lower case
        user_response = input(question).lower()

        for item in valid_ans:

            # check if the user response is a word in the list
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

            # print error if user enters invalid
        print(error)
        print()


# main routine

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Would you like to see the instructions? ")

print(f"You say", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You chose ", user_choice)
