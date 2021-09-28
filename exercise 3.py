"""3. Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old."""
from datetime import datetime
t=datetime.now()
year = t.year
name = str(input("enter your name"))
age = int(input("enter your age"))
print("you will be turning 100 in the year",year+(100-age))