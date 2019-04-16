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