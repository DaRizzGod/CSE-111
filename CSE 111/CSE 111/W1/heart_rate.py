"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input('What is your age?'))

max_heart_rate = 220 - age
max_excerise_rate = max_heart_rate * .85
min_exceise_rate = max_heart_rate * .65

print(f'Your ideal excerise heart rate is between {min_exceise_rate:.0f} and {max_excerise_rate:.0f} beats per minute.')
