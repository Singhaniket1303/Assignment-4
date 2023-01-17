# ques 1

marks=float(input("Enter marks of the student "))
if marks<25 and marks>=0 :
    print("Grade is F")
elif 25<=marks and marks<45 :
    print("Grade is E")
elif 45<=marks and marks<50 :
    print("Grade is D")
elif 50<=marks and marks<60 :
    print("Grade is C ")
elif 60<=marks and marks<=80 :
    print("Grade is B")

elif marks>80 and marks<=100:
    print("Grade is A")
else :
    print("Marks are not in the range from 0 to 100")

# ques2

year= int(input("Enter an Year "))
if year%100!=0 and year%4==0 :
    print("Year is a Leap Year")
elif year%100==0 and year%400==0:
    print("Year is a Leap Year")
else:
    print("Year is not a Leap Year")

# ques 3

import random
i=1
print("Hello Welcome to this Multiplication game answer the following")
while i<=10 :
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1,"X",num2)
    ans1 = int(input("Enter Answer"))
    if ans1 == num1 * num2:
        print("Well done,Right Answer")
    else:
        print("Sorry Wrong Answer")
    i = i + 1

# Ques 4

for candy in range(200):
    if candy%5==2 and candy%6==3 and candy%7==2:
      print(candy)