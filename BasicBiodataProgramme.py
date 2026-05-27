#biodata 

#asking for name 
name = input("what is your name, dear?")

#asking for father's name
father_name = input("what is your father's name?")

#asking for mobile no. 
mobile_no = input("what is your mobile no. dear?")

#asking for age 
age = input ("tell me your age")
if int(age)<18:
    print("you are pretty young, Great!")
else: print(f"Ohh {age}, congratulations responsible adult!")

#asking for roll no.
roll_no = input ("now what is your role no")

#telling to wait 
print("you are just there, few more info")

#asking for school name 
school_name = input("now tell me your school's name")

print ("done!")

print("BIODATA -", f"Name of the student: {name}", f"Age of the Student: {age}", f"Roll No. of the Student: {roll_no}", f"School Name: {school_name}", f"Father's Name: {father_name}", f"Mobile No.: {mobile_no}", sep = "\n")


"""
this print command will print the biodata in the format shown below
BIODATA -
Name of the student: 
Age of the Student: 
Roll No. of the Student: 
School Name: 
"""

