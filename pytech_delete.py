"""
    Title: pytech_delete.py
    Author: Salahauddin Faisal
    Date: 21 February 2021
    Document: Program to delete documents from the connected Database Collections
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


# Creating test students document to perform delete operation
 
test_student = {
    "_id": "2005",
    "First Name": "Kamal",
    "Last Name": "Chowdhury"
}

try:
    students.insert_one(test_student)
except pymongo.errors.DuplicateKeyError:
    pass 


# Finding the new student(test_student) using find_one() method
test_student_info = students.find_one({"_id": "2005"})

print("Newly inserted student's  Information \n")

print("Student ID: " + test_student_info["_id"] + "\nFirst Name: " + test_student_info["First Name"] + "\nLast Name: " + test_student_info["Last Name"])

# Deleting the newly created test_student
students.delete_one({"_id": "2005"})

# Listing all students in the Database after the deletion of test_student
print("\n -- New Students List after Deletion of the test Student --\n")
# find all students in the collection 
all_student = students.find({})

# Dispaying all the students information from the Database
print(" -- Displaying all the students information --\n")
for student in all_student:
    print("Student ID: " + student["_id"] + "\nFirst Name: " + student["First Name"] + "\nLast Name: " + student["Last Name"])
    print()

print("\n --- END OF PROGRAM ---")

