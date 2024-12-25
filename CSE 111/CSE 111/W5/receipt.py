import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    products_dict = {}
    try:
        with open(filename,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[key_column_index]
                products_dict[key] = row
    except FileNotFoundError:
        print('The file was not found.')
    return products_dict

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        print('Store Name')
        print('Requested items')
        total_items = 0
        subtotal = 0.0 
        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                if product_number in products_dict:
                    product = products_dict[product_number]
                    price = float(product[2])
                    print(f'{product[1]}: {quantity} @ {price}')
                    total_items += quantity
                    subtotal += quantity * price
        print(f'Total items: {total_items}')
        print(f'Subtotal: {subtotal}')
        tax = subtotal * 0.06
        print(f'Sales tax: {tax}')
        total_due = subtotal + tax
        print(f'Total due: {total_due}')
        print(f'Thank you for your incredible donation to the Wally World of America!')
    except KeyError:
        print('A Key error occurred.')
    current_date_and_time = datetime.now()
    print(f"Current date and time: {current_date_and_time:%A %I:%M %p}")

if __name__ == '__main__':
    main()
