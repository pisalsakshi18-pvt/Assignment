
# 1 Program to check whether a number is positive, negative

#num = int(input("Enter a number:"))

#if num > 0:
#     print("The number is Positive")
#else:
#    print("The number is Negative")


# 2 Write a program to check whether a number is even or odd

#num = int(input("enter a number:"))
#if num  % 2 == 0:
 #   print("the number is even")
#else:
 #   print("the number is odd")    



# 3 Write a program to find the greater number between two numbers

#num1=int(input("enter number1:"))
#num2=int(input("enetr number2:"))

#if num1 > num2:
    #print("Greater number1 is num1")
#elif num2 > num1:
    #print("greater number2 is num2")
#else:
    #print("both umber are equel")       

# Program to check voting eligibility


# 4 Write a program to check whether a person is eligible to vote (age ≥ 18)

#age = int(input("Enter your age:"))

#if age >= 18:
    #print("You are eligible to vote")
#else:
 #   print("You are not eligible to vote")

 

# 5 Write a program to check whether a number is divisible by 5



#num = int(input("Enter a number:"))

#if num % 5 == 0:
 #   print("The number is divisible by 5")
#else:
 #   print("The number is not divisible by 5")


# 6 Write a program to check whether a given year is a leap year or not


#year = int(input("Enter a year: "))

#if  (year % 4 == 0 )
 #   print("It is a Leap Year")
#else:
 #   print("It is not a Leap year")



# 7 Write a program to check whether a character is a vowel or a consonant


#ch = input("Enter a character:")

#if ch in 'aei':
 #   print("it is a vowel")
#else:
 #   print("it is a consonant")


# 8 Write a program to find the largest among three numbers

#num1 = int(input("enter number1"))
#num2 = int(input("enter number2"))
#num3 = int(input("enter number3"))

#if num1 > num2:
 #   if num1 > num3:
  #      print("num1 is greater")
   # else:
    #    print("num3 is greater")
#else:
 #   if num2 > num3:
  #       print("num2 is greater ")
   # else:
   #  print("num3 is greater")      



# 9 Write a program to assign grades based on marks
#90 and above → A 
#75 to 89 → B 
#50 to 74 → C 
#Below 50 → Fail 


#marks = int(input("Enter your marks:"))

#if marks >= 90:
    #print("Grade:A")
#elif marks >= 75:
    #print("Grade:B")
#elif marks >= 50:
    #print("Grade:C")
#else:
    #print("Grade:Fail")


#10 Write a program to check whether a number is within the range of 1 to 100

#num = int(input("Enter a number "))

#if 1 <= num <= 100:
 #   print("The number is within the range of 1 to 100")
#else:
 #   print("The number is outside the range of 1 to 100")


# 11 Write a program to print numbers from 1 to 10 using a for loop


#for i in range(1 , 11):
 #   print(i)


# 12 Write a program to print numbers from 10 to 1 in reverse order

#for i in range(10 , 0, -1):
#    print(i)


# 13 Write a program to print numbers from 10 to 1 in reverse order

#for i in range(1 , 21):
 #   if i % 2 == 0:
  #      print(i)


# 14 Write a program to print all odd numbers between 1 and 20


#for i in range(1 , 21):
 #   if i % 2 != 0:
  #      print(i)


# 15 Write a program to find the sum of numbers from 1 to 100


#sum = 0
#for i in range(1 , 101):
    #sum = sum +i
#print("Sum of numbers from 1 to 100 is:",sum)



# 16 Write a program to print the multiplication table of a given number


#num = int(input("enter a number:"))

#for i in range(1, 11):
#    print(num, "x", i, "=", num * i)



# 17 Write a program using nested for loops to print pattern


#for i in range(5):
 #   for j in range(5):
  #      print("*" , end=" ")

   # print()



# 18 Write a program to print each character of a string using a for loop

#ch = "sakshi"

#for i in range(0 , len(ch)):
 #   print(ch[i])



# 19 Write a program to find the factorial of a given number using a for loop
#num = int(input("enter a number"))

#fact = 1
#for i in range(1, num ,+1):
 #   fact *=i
  #  print("fact" , num ,"is:",fact)



# 20 Write a program to print the following pattern
 
#n = 5
#for i in range(1, n + 1):
 #   print("*" * i)



#21 Write a program to print numbers from 1 to 10 using a while loop

# a = 1
# while a<=10:
 #   print(a)
  #  a=a+1



# 22  Write a program to print numbers from 10 to 1 in reverse order using a while loop

#i = 10
#while i >= 1:
 #   print(i)
  #  i -=1



# 23 Write a program to print all even numbers between 1 and 20 using a while loop


# a = 1
# while a < 21 :
#    if a % 2 == 0:
 #       print(a)
  #  a = a+1


# 24 Write a program to print all odd numbers between 1 and 20 using a while loop

# a = 1
 # while a < 21:
   # if a % 2 != 0:
    #    print(a)
   # a = a+1


# 25 Write a program to find the sum of numbers from 1 to 100 using a while loop


# sum = 0
# i = 1
# while i <= 100:
  #  sum = sum + i
   # i = i + 1
   # print("sum of numbers from 1 to 100:",sum)


# 26 Write a program to print the multiplication table of a given number using a while loop

#num = int(input("Enter a number: "))

#i = 1
#while i <= 10:
 #   print(num, "x", i, "=", num * i)
  #  i += 1



# 27 Write a program to count the number of digits in a given number using a while loop



#num = int(input("enter a number"))
#count = 0

#while num > 0:
 #   num = num // 10
  #  count = count +1
#print("number of digits =", count)


# 28 Write a program to reverse a given number using a while loop

#num = int(input("Enter a number: "))

#reverse = 0

#while num > 0:
 #   digit = num % 10          
  #  reverse = reverse * 10 + digit
   # num = num // 10           

#print("Reversed number:", reverse)



# 29 Write a program to find the factorial of a given number using a while loop

#num = int(input("Enter a number: "))

#fact = 1
#i = 1

#while i <= num:
 #   fact = fact * i
  #  i = i + 1
#print("Factorial =",fact)


# 30 Write a program to keep asking the user for a password until the correct password is entered


#correct_password= "123456"

#password = input("Enter password: ")

#while password != correct_password:
 #   print("try again")
  #  password = input("Enter password: ")

#print("successful")