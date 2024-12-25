# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's sex, birthdate, height, and weight.
user_sex = input('What is your sex, male or female? ')
user_age = compute_age(input("What is your bithday? (YYYY-MM-DD) "))
user_weight_kg = compute_kg_from_lb(float(input("What is your weight? (US pounds)")))
user_height_cm = cm_from_in(int("How tall are you in inches? "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
	user_bmi = body_mass_index(user_weight_kg, user_height_cm)
    user_bmr = basal_metabolic_rate(user_sex, user_weight_kg, user_height_cm, user_age)
    # Print the results for the user to see.
    print(f"Age: {user_age}.\nWeight: {user_weight}KG.\nGender: {user_gender}\nBody mass index: {user_bmi}.\nBasal metabolic rate (kcal/day): {user_bmr}.")
# Age (years): 17
# Weight (kg): 65.77
# Height (cm): 147.3
# Body mass index: 30.3
# Basal metabolic rate (kcal/day): 1580

   
def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return pounds * 0.45359237 


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return inches * 2.54


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return 10000 * weight / height ** 2


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == 'male':
      bmr = 88.362 + 13.397 * weight + 4.799 * height − 5.677 * age
    elif gender.lower() == 'female':
      bmr = 447.593 + 9.247 * weight + 3.098 * height − 4.330 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()

print("Thanks for the help, Miles!")
# # this program will start executing.
