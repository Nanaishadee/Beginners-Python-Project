# Strings
# Creating a new line
print("Hi! I am Nana \n I must get a hang of this course")
 # Quotation in between quotation
print("Nana\'s sister is fine")
#Concatenation
phrase = "Nana Braimoh "
print(phrase + "is fun to be with")
#using functions
print(phrase.upper())
print(len(phrase))
print(phrase[0:4])
#Index starts with zero
print(phrase.index("B"))
print(phrase.replace("Nana", "Halima"))

#Getting Input From Users
name = input("Enter your name: ")
print("Hola " + name + " !") 
#Making a List
friends = ["Anu"," Rachael", " Temi"]
print(friends[-2])
#Using list functions
lucky_number = [2, 5, 8, 10, 15, 20]
friends = ["Anu"," Rachael", " Temi", "Mercy", "Tola", "Oyin"]
friends.extend(lucky_number)
friends.append("Nana")
print(friends)
#Tuples are immutable
coordinates = (3, 6)
print(coordinates[0])
#Functions
def game(name):
    print(name + " " + "Space Invaders")
game("Nana")
#Return
def cube(num):
    return num ** 2
result = cube(10)
print(result)
# If Statements
is_female = True
is_beautiful = False
if is_female: 
    print("You are a female")
elif is_female and not (is_beautiful):
    print("Wow I love you")
else:
    print("Not a female")
#Comparisons
def min_num(num1, num2, num3):
    if num1 < num2 and num2 > num1:
        return num2
    elif num3 <= num1 and num1 > num3:
        return num1
    else:
        return num3
result = min_num(300, 45, 20)
print(result)

