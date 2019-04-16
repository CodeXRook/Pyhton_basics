age = 24
print("My age is" + str(age) +' '"years")#WORKS IN INTELLIJ

print("My age is {0} years".format(age))#WORKS IN INTELLIJ

print("There are {0} days in {1}, {2}, {3}, {4}, {5} {6} and {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))#WORKS IN INTELLIJ

#Concept of replacement field.
print("""January:{2}
February:{0}
March:{2}
April:{1}
May:{2}
June:{1}
July:{2}
August:{2}
September:{1}
October:{1}
November:{1}
December:{2}""".format(28, 30, 31))

print("My age is %d years" % age)#WORKS IN INTELLIJ
print("My age is %d %s, %d %s" %(age, "years", 6, "months"))#WORKS IN INTELLIJ


for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))#WORKS IN INTELLIJ #reaplacement field number

print("Pi is approximately %12f" % (22 / 7))#WORKS IN INTELLIJ #SPECIFY THE PERCISION OF A NUMBER
print("Pi is approximately %12.50f" % (22 / 7)) #SPECIFY THE PERCISION OF A NUMBER

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

first_name = "John"
last_name = "Cleese"
age = 78
print(first_name + '  ' + last_name +'  ' + str(age))#STR(AGE) WORKS LIKE PARSiNT()TURN A NUMBER TO A STRING TO ADD THE VALUE OF THAT NUMBER TO A STRING