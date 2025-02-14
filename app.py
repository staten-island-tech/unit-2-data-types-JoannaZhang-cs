""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

# Print the element 7
""" print(values[3])  # This prints 7

x = "this is a thing"
y= x.split( ) #split() separates the string at any whitespace (spaces, newlines, etc.)
z = y[0]
print(y)
print(z) """

#booleans
""" def login(password):
    #if statement evaluates to true we go to next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect")
x = input("what is the password")
login(x) """

""" def grade(score):
    if score >=92:
        print("A")
    elif score>= 82:
        print("B")
    elif score >= 72:
        print("C")
    else:
        print("F")
#add integer (int) if you need the answer to be an integer
x = int(input("what is the score"))
grade(x) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" 
x = "test"
print(f"hello {x}")

temp = 68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def gamble(age, id):
    if age >= 21:
        if id:
        #if id == True means the same thing
            print("Gamble away")
        else: 
            print("You need Id verification")
    else:
        print("You're too young")
 """

""" def gamble(age, id):
    if age >= 21 and id == True
    #if id == True means the same thing as if id
        print("have fun")
    elif age >= 21 and id == False: 
        print("You need Id verification")
    else:
        print("You're too young")
 """
""" raining = True
if raining == True:
    print("stay home")
if raining == False:
    print("go for walk")
#these are the same """



#odd and even test

#% gives you the remainder

""" x = "test"
print(f"number {x}")


number = int(input("What is the number?"))

if (number % 2) == 0:
    print('even')
else: 
    print('odd') """


#bill challenge

""" # Ask for the rating
service = input ("How was the service?")
# Call the function to display the bill percentage
def bill(service):
    if service.lower() == "bad":
        print("0%")
    elif service.lower() == "okay":
        print("15%")
    elif service.lower() == "good":
        print("20%")
    else:
        print("25%")
bill(service)
#RUN THE CODE!!!! (BILL(SERVICE)) """



#Create a function that accepts an input and determines all factors of the number.

""" def find_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors
print(find_factors(15))

#check i X is a factor Modulo
#if factor == true add to list
#loop from 2 to Y for i in range(2,15)
#if  x isFactor and y isFactor then add to list """



#Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.

def find_gcf(num1,num2):
    while num2 > 0:
    #!= means not equal
        num1, num2 = num2, num1 % num2
    return num1
print(find_gcf(20,35))


#REVIEW ABOVE CODE!!!!!!