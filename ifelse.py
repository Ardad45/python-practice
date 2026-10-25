a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a>b:
    print(a," is greater than ",b)
else:
    print(b," is greater than ",a)
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
char=input("Enter a character: ")
if char in ('a','e','i','o','u','A','E','I','O','U'):
    print(char," is a vowel.") 
else:    print(char," is a consonant.")
num=int(input("Enter a number: "))
if num%2==0:
    print(num," is an even number.")
else:
    print(num," is an odd number.")
num=int(input("Enter a number: "))
if num>0:
    print(num," is a positive number.")
elif num<0:
    print(num," is a negative number.")
else:    print(num," is zero.")
n=int(input("Enter a number: "))
if n%5==0 and n%7==0:
    print(n," is divisible by both 5 and 7.")
elif n%5==0:
        print(n," is divisible by 5 but not by 7.")
elif n%7==0:
        print(n," is divisible by 7 but not by 5.")
else:
    print(n," is not divisible by both 5 and 7.")
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")
username=input("Enter your username: ")
if username=="pranav":
 password=input("Enter your password: ")
 if password=="prnav123":
    print("Login successful.")
 else:
    print("Incorrect password.")
else:
   print("Username not found.")
