n1=float(input("Enter Marks in  Mathematics:"))
n2=float(input("Enter Marks in  Filipino:"))
n3=float(input("Enter Marks in  Science:"))
n4=float(input("Enter Marks in  Physical Education:"))
n5=float(input("Enter Marks in  Practical Research:"))
n6=float(input("Enter Marks in  Araling Panlipunan:"))
n7=float(input("Enter Marks in  Edukasyon sa Pagpapakatao:"))
n8=float(input("Enter Marks in  Personal Development:"))
n9=float(input("Enter Marks in  Philosophy:"))
n10=float(input("Enter Marks in  Political Science:"))
n11=float(input("Enter Marks in  Applied Economics:"))
n12=float(input("Enter Marks in  Reading and Writing:"))

sum=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
print("The Sum is:", sum)

percentage=(sum/1200)*100
print("The percentage is:", percentage)

#Grading Line
if percentage>=90:
    print("A+")

elif percentage>=80:
    print("A")

elif percentage>=70:
    print("B+")

elif percentage>=60:
    print("B")

elif percentage>=50:
    print("C+")

elif percentage>=40:
    print("C")

elif percentage>=30:
    print("D+")

else:
    print("Failed")
