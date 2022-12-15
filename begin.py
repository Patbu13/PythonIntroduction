#   Patrick Burroughs
#   Dec 15 2022
print("Hello " "World")

myNum = 3
print(myNum)

myNum = "Yo" * 3 + " oooy"
print(myNum)

nums = []
nums.append(13.47)
nums.append("magic")
print(nums)

""" yoloo
yoolo """

name = input("Name please: ")
print("What's up, ", name)

# accept strictly integer from the user
needInt = int(input("Enter num: "))
print("Square it!", needInt**2)

# modulus jawn
# and do whiles don't exist!
# I N D E N T A T I O N
while True:
    modo = int(input("gimme your best number: "))
    if(modo % 12 == 0):
        print("dozenable!")
    elif(modo % 6 == 0):
        print("halfly dozenable i guess")
    else:
        print("mid ass number,", modo // 12, "when divided by 12, remainder of", modo % 12, ", goodbye")
        break

# funciones
def func1():
    print('this')
    print('is')
    print('it')
func1()