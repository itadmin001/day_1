######################  Exercise #1

error = "Read the instructions and try again dum dum!"
x=''
y=''


while True:
    try:
        x, y = (input("Enter 2 ages, the oldest one first, separated by a space or 0 0 to quit: ")).split()
    except KeyboardInterrupt:
        print("CTRL-C Pressed. Exiting...")
        exit()
    except:
        print(error+" You must enter two values!")
        continue
    if x.isnumeric() and y.isnumeric():
        if int(x) == 0 and int(y) == 0:
            break
        else:
            age1,age2 = int(x), int(y)
        if age1 >= age2:
            diff = age1 - age2
            print(f"The the difference between {str(age1)} years old and {str(age2)} years old is: {str(diff)} years")
            break
        else:
            print(error+f" {age1} is not greater than or equal to {age2}!")
    else:
        print(error +f" At least one of your inputs in not a number!")

        


######################  Exercise #2


import random

verbs = ['abandoning', 'accusing','adopting','dancing with', 'debugging', 'defending','demanding','tackling','relaxing with', 'repairing','riding','roasting']
adjectives = ['an amazing', 'an awkward','an ancient','an edible','an errie','an effeminate','a kind-hearted','a knurled','a rabid', 'a raging','a rank','a raspy']
nouns2 = ['stray dog','feral cat','cross-eyed gazelle','wounded rat','homless man','dead bird','wizard','sasquatch','billy goat']

try:
    while True:
        noun = " "
        verb = " "
        adjective = " "
        noun2 = " "

        noun = input("Enter your name or 'quit' to exit: ")
        if noun.lower() == 'quit':
            print("Thanks for playing!")
            break
        place = input("Name a place of business or \n"
                      "someone's house that you know: ")

        #generate the pieces:
        verb = verbs[random.randrange(0,len(verbs))]
        adjective = adjectives[random.randrange(0,len(adjectives))]
        noun2 = nouns2[random.randrange(0,len(nouns2))]


        string = f"{noun}, was seen {verb} {adjective} {noun2} out behind {place}"
        print(string)

except KeyboardInterrupt:
    print(f"\n Thanks for playing!")
except UnboundLocalError:
    print("Unhandled Exception")



######################   Exercise #3

age = ''
while True:
    try:
        age = int(input("Enter Your Age: "))
    except KeyboardInterrupt:
        print("\nCTRL-C Pressed. Exiting...")
        exit()
    except:
        print("Connot be blank and must be a number")
        continue
    if age < 18:
        print(f"You're only {age}...You're just a kid!")
        break
    elif age >= 18 and age < 65:
        print(f"You're {age}...aren't you a grown-ass person!")
        break
    else:
        print(f"Geez, {age}...you're pretty old there Mr. Senior Citizen")
        break




######################   Exercise #4


from math import *

x=int(input("Is this number a square?: "))

print(f"The square root of {x} is {int(sqrt(x))}") if isqrt(x)*isqrt(x)==x else print(f"{x} is not a square number")







######################   Exercise #5 


word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

words = ["panini","bulbasaur","pie","dolphin","dog"]

for word in words:
    if len(word) > 5:
        print("TRUE")
    else:
        print("FALSE")