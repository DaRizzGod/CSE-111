import math

height = float(input("what is the hight of you pendulum in inches? "))

def P_time(height):
    time = 2 * math.pi * math.sqrt(height / 9.81)
    return time

print(f"{P_time(height):.2f}")