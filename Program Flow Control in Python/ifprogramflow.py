name = input("Please enter your name:")
age = input("How old are you, {0}? ".format(name))
print(age)

name = (input("Please enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
    
if age >= 18:
    print("You are old enough to vote")
 else:
    print("Please come back in {0} years".format(18 - age))

#USING INPUT TO IN IF AND ELSE
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    if guess > 5:
        print("Ok Now you're getting close, try again.")
        guess = int(input())
    if guess > 5:
        print("Just start over")
    else:
        print("no good") #IT WORKS BUT I WANT TO DO SOMETHING ELSE

#DIFFENT TEST CASE FOR IF, ELSE AND ELIF.
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")
elif guess > 5:
    print("Please guess lower") 
    guess = int(input())
    if guess == 5:       
