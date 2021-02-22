"""
    Title: pytech_update.py
    Author: Salahauddin Faisal
    Date: 21 February 2021
    Document: Program to make updates on the connected Database Collections
 """

import pymongo
from pymongo import MongoClient

# Connecting to MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.o4awn.mongodb.net/students?retryWrites=true&w=majority"
client = MongoClient(url)
# Linking Database with client object
db = client.pytech
students = db.students

# find all students in the collection 
all_student = students.find({})

# Dispaying all the students information from the Database
print("\n -- Displaying all the students information --\n")
for student in all_student:
    print("Student ID: " + student["_id"] + "\nFirst Name: " + student["First Name"] + "\nLast Name: " + student["Last Name"])
    print()

# update student_id 1007
a_student = students.update_one({"_id": "1007"}, {"$set": {"Last Name": "Baskin"}})

# find the updated student document 
t_baskin = students.find_one({"_id": "1007"})

# display message
print("\n -- Showing info for student with _id 1007 --")

# output the updated document to the terminal window
print("Student ID: " + t_baskin["_id"] + "\nFirst Name: " + t_baskin["First Name"] + "\nLast Name: " + t_baskin["Last Name"])


