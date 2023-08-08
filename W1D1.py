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
from tkinter import *
global flag

flag=False

def display_lib(v,a,n2):

    v,a,n2=randomize()
    
    n=name_entry.get()
    p=place_entry.get()

    pu_window = Toplevel(win)
    pu_window.title("LMAO!")

    pu_frame = Frame(pu_window)
    pu_frame.pack(padx=20,pady=20)

    message = n+" "+"was seen"+" "+v+" "+a+" "+n2+" "+"out behind"+" "+p

    output_label = Label(pu_frame,text=message,font=('Helvetica','14','bold'))
    output_label.grid(row=1,column=1)

def randomize():
    verbs = ['abandoning', 'accusing','adopting','dancing with', 'debugging', 'defending','demanding','tackling','relaxing with', 'repairing','riding','roasting']
    adjectives = ['an amazing', 'an awkward','an ancient','an edible','an errie','an effeminate','a kind-hearted','a knurled','a rabid', 'a raging','a rank','a raspy']
    nouns2 = ['stray dog','feral cat','cross-eyed gazelle','wounded rat','homless man','dead bird','wizard','sasquatch','billy goat']

    verb = verbs[random.randrange(0,len(verbs))]
    adjective = adjectives[random.randrange(0,len(adjectives))]
    noun2 = nouns2[random.randrange(0,len(nouns2))]

    return verb,adjective,noun2

win = Tk()
win.title("Get R Done")

win_frame = Frame(win)
win_frame.pack(padx=20,pady=20)

name_entry_label = Label(win_frame,text="Enter Your Name: ")
name_entry_label.grid(row=1,column=0)

name_entry = Entry(win_frame,width=30)
name_entry.grid(row=1,column=1)

place_entry_label = Label(win_frame,text="Name of a place of business or \n"
                "someone's house that you know:")
place_entry_label.grid(row=2,column=0)

place_entry = Entry(win_frame,width=30)
place_entry.grid(row=2,column=1)

verb,adjective,noun2 = randomize()

submit_btn = Button(win_frame,text="Submit",command=lambda: display_lib(verb,adjective,noun2))
submit_btn.grid(row=4,column=1)

win.mainloop()



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