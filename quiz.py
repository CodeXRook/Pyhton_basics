#Question 1:
#The following program contains an error.  Examine the code carefully, and work out which line is incorrect:
print("Python was created by Guido van Rossum.")
print("He's referred to as the BDFL,")
print("the "Benevolent Dictator For Life"")#ANSWER
print("and has the final word when it comes to enhancements to Python.")
#The speech marks aren't right, because the string contains " characters, and is also delimited with "


#Question 2:
#In this program, 2 of the variables will have the same value
eal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""
# MEALS2 ANd MEALS4


#Question 3 :
#What will be the output produced by this line?
print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")
    #Terry	John	Graham	Michael	Eric	Terry

#Question 4:
#What will be the output of this program?
first_name = "John"
last_name = "Cleese"
age = 78
 print(first_name + last_name + age)
#THIS WI;; THROW ERROR,numerical values can't be added to strings.YOU MUST USE str(age).


#Question 5:
#What result will this program print?
a = 45
b = 15
c = 3
 
print(a - b / c)
#40.0
#b / c will be calculated first, to give 45 - 5.0 Because the division gives a float, the result will also be a float.


#Question 6:
#What output will this program produce?

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)
#50.0
#The Total including tax is calculated, but isn't printed. The value of total doesn't include the tax.


#Question 7:
#What will this program print?

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

#MTWTFSS
#The slice starts at the first character, and includes every 5th character.



