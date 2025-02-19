# Check that users have entered a valid
# option based on a list
def string_checker(user_response, valid_ans):
    while True:

        # get user response and make sure its lower case
        user_response = user_response.lower()

        for item in valid_ans:
            
            # check if the user response is a word in the list
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        return "Invalid"


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    (0, 'invalid'),
    (1, 1),
    (2, 2),
    ('enter', 'infinite'),

]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
