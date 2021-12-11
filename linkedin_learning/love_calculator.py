import collections

"""
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
    "Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
    "Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
    "Your score is **z**."
"""

while True:
    print("*************************************")
    if input("Welcome to the Love Calculator! Enter 0 to quit or hit enter to continue->") == '0':
        print("Thanks you for your interest!! Visit again.")
        break
    name1 = input("Enter your name? \n")
    name2 = input("Enter your love's name? \n")

    combined_name = (name1 + name2).lower()
    counts = dict(collections.Counter(combined_name))
    true = str(sum([v for k, v in counts.items() if k in 'true']))
    love = str(sum([v for k, v in counts.items() if k in 'love']))

    if int(true + love) > 90 or int(true + love) < 10:
        print(f"Your score is {true + love}, you go together like coke and mentos.")
    elif 40 < int(true + love) < 50:
        print(f"Your score is {true + love}, you are alright together.")
    else:
        print(f"Your score is {true + love}.")
