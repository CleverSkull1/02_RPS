# Choose the game goal as a value that's > 13
def int_check(to_check):
    """Checks users enter an integer more than or equal to 1"""
    while True:
        error = "Please enter an integer more than or equal to 13. "

        if to_check == "":
            return "infinite"
        try:
            response = int(input("Choose a game goal "))

            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"


# main routine starts here
target_score = int_check()
print(target_score)
