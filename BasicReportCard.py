#asking student's name 
name = input("Tell me your name dear ")
print("That's a great name! ")

#asking their's class
standard = input("Okay, now tell me the standard you study in ")


#asking their 3 favorite subject 
print ("What are your favorite subject? Tell me any three of them ")
fav_subject1 = input("1st favorite subject ")
fav_subject2 = input("2nd favorite subject ")
fav_subject3 = input("3rd favorite subject ")

print ("Ohh!", fav_subject2, "You have great choices!!")
print("You are soo close,")


#asking their's marks out of 100
print("Just now tell the marks you scored in all your three subjects.. ")
marks1 = int(input ("Your score in " + fav_subject1, end = " "))
marks2 = int(input ("Your score in " + fav_subject2, end = " "))
marks3 = int(input ("Your score in " + fav_subject3, end = " "))


"""
to be printed as 

-----------REPORT CARD-----------
Student Name -> Dhruv 
Class -> 10th
Subject 1 -> Maths Marks -> 85
subject 2 -> Science Marks -> 90
Subject 3 -> English  Marks -> 78 
----------------------------------
Total Marks -> 253 out of 300
Thank you Dhruv, Keep it up!

"""

#final resulting convo and design of report card
print("Now this programme will generate your Report Card, Please Wait")


print("-----------REPORT CARD-----------")

print("Student Name ->", name)
print("Class ->", standard)
print("Subject 1 ->", fav_subject1, "Marks ->", marks1)
print("Subject 2 ->", fav_subject2, "Marks ->", marks2) 
print("Subject 3 ->", fav_subject3, "Marks ->", marks3)

print("----------------------------------")

total = marks1 + marks2 + marks3
print("Total Marks ->", total, "Out of 300", "Keep it up!")




