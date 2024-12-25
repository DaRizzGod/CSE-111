import math


    
def compute_storage_efficiency(volume, surface_area):
storage_efficiency = volume / surface_area

return storage_efficiency

def compute_volume(radius, height):

volume = math.pi * radius **2 * height
return volume


def compute_surface_area(radius, height):

surface_area = 2*math.pi * radius (radius + height)
return surface_area

def main():

with open("can.txt", "r") as files:
    files.readline()    
    for file in files:
        file = file.strip()
        data = file.split(" ")
        name = file_data[0]
        radius = float(file_data[1])
        height = float(file_data[2])
        cost = float(file_data[3])
        
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    
print(f"The can name is {name}")
print(f"The can radius: {radius}")
print(f"The can height: {height}")
print(f"The can cost: {cost}")
print(f"The can volume: {volume}")
print(f"The can surface area: {surface_arae}")
print(f"The can storage efficiency: {storage_efficiency}")
main()







           