import math
from datetime import datetime
current_date_and_time = datetime.now()

print("Welcome to CSE 111 auto reapir shop!")
      
w = int(input('What is the width of the tires? '))
a = int(input('What is the aspect ratio of the tire? '))
d = int(input('What is the diameter of the wheel? '))
t = f'{current_date_and_time:%Y-%m-%d}'

air = math.pi * w**2 * a * (w * a + 2540 * d)/ 10000000000

print(f'The approximate volume is:{air:.0f} liters')
    
print(f'{current_date_and_time:%Y-%m-%d}')
print(f'{t}, {w}, {a}, {d}, {air}')


with open('volumes.txt', "at") as volumes_file:
    

    print(f'{t}, {w}, {a}, {d}, {air}',file=volumes_file)
    
    
    

