#happy = True

#if happy == True:
#    print("Awesome!")

print("What is your age?")
age = int(input())
#can_drink = age > 21 #another age variable that can be assigned so we can check against it.
#print(can_drink)

if  65 > age > 21:
    print("Welcome to our app, can drink for sure!!")
elif age < 21:
    print('Can\'t drink you\'re under the age')
elif age > 65: #a catch-all statement
    print("You're a senior citizen")
else:
    print("Super special!")

print("Thaaaaanks!")