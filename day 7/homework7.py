
x = 1
while x <= 100:
    x = x * 2
    print(x)


for i in range(1, 10 +1 ):
    if i == 8: break
    print(i)


for num in range(1, 100):
    if num % 4  == 0:
     print(num)



name = input("enter your name: ")
print("you are ", name)

lastname = input("enter your lastname: ")
print("your lastname is", lastname)

age = input("enter your age: ")
print(f"you are {age} years old")

country = input("enter your country: ")
print("you live in", country)



num1 = int(input("enter number: "))
num2 = 17
while num1 < num2:
   print("the number is too low try again!")
   num1 = int(input("enter number:"))

if num1 > num2 :
   print("the number is too high try again!")
   num1 = int(input("enter number:"))

elif num1 == num2:
   print("you have guessed the number ")


