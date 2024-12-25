import datetime
import string
import random

class User:
    def __init__(self, name, gender, age, location):
        self.name = name
        self.gender = gender
        self.age = age
        self.location = location

    @staticmethod
    def get_user_name():
        return input("Please enter your name:")

    @staticmethod
    def generate_gender():
        return random.choice(['Male', 'Female'])

    @staticmethod
    def get_user_age():
        return input("Please enter your age:")

    @staticmethod
    def get_user_location():
        return input("Please enter your location: ")

    def print_user_info(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

user = User(User.get_user_name(), User.generate_gender(), User.get_user_age(), User.get_user_location())
user.print_user_info()

current_datetime = datetime.datetime.now()

print(f'My name is: {user.name} and I am a {user.gender}. I happen to be {user.age} years old but I am from {user.location}.')

print('Thank you again for all you do and the amount of you have been this semester. I hope the best for you and the next semester!')