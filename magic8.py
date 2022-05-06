import random

# taking in user's inputs:
name = input("What is your name ? ")
question = input("What is your question " + name + " ? ")

# initialisation of the answer variable:
answer = ""

# random number is generated
random_number = random.randint(1, 9)

# if you also want to see the random number printed, un-comment the following:
# print(random_number)

# answer updates using the random_number::

if random_number == 1:
    answer += "Yes - definitely."
elif random_number == 2:
    answer += "It is decidedly so."
elif random_number == 3:
    answer += "Without a doubt."
elif random_number == 4:
    answer += "Reply hazy, try again."
elif random_number == 5:
    answer += "Ask again later."
elif random_number == 6:
    answer += "Better not tell you now."
elif random_number == 7:
    answer += "My sources say no."
elif random_number == 8:
    answer += "Outlook not so good."
elif random_number == 9:
    answer += "Very doubtful."
else:
    print("Error")


# if question isn't provided by user, prints out warning message.
# if name isn't provided by user and question is provided, outputs the question without the name.
# if question and name are provided, answer shall be given.

if question == "":
    print("If no question is provided to the all-mighty, no answer shall be given.")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball' answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
