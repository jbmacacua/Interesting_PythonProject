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