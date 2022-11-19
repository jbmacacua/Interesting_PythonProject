print("____________________________________________________________________________________\n")
print("This is the reference video link: https://www.youtube.com/watch?v=DLn3jOsNRVE&t=185s")
print("\n____________________________________________________________________________________")

#ask the user
print("\n|======= Welcome to my Quiz Game =======|")
playing = input("\nDo you want to play? ")

#if playing = yes
print("\nOkay! Let's play :)")

#Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Quesion 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('*****  Correct!  *****\n')
    score += 1
else:
    print("*****  Incorrect!  *****\n")

#Quesion 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('*****  Correct!  *****\n')
    score += 1
else:
    print("*****  Incorrect!  *****\n")

#Quesion 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('*****  Correct!  *****\n')
    score += 1
else:
    print("*****  Incorrect!  *****\n")