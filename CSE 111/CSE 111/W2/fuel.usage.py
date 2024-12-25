def main():
    first_odometer = int(input('Please enter the first odometer reading (miles): '))
    second_odometer = int(input('Please enter the second odometer reading (miles): '))
    fuel_amount = float(input('Enter the amount of fuel used (gallons): '))
    mpg = miles_per_gallon(first_odometer, second_odometer, fuel_amount)
    lp100k = lp100k_from_mpg(mpg)
    
    print(f'Your miles per gallon is {mpg:.2f}')
    print(f'Your liters per 100k is {lp100k:.2f}')
    
def miles_per_gallon(first_odometer,second_odometer, fuel_amount):
    return (second_odometer - first_odometer) / fuel_amount

def lp100k_from_mpg(mpg):
    return 235.215/mpg
    

main()