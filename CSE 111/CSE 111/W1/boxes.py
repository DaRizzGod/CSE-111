import math

def get_boxes_needed(items_per_box, total_items):
    number_of_boxes = total_items / items_per_box
    return math.ceil(number_of_boxes)

total_items = int(input('Enter the number of items: '))
items_per_box = int(input("Enter the number of items per box: "))

boxes_needed = get_boxes_needed(items_per_box, total_items)

print(f'For {total_items} items, packing {items_per_box} items in each box, you will need {boxes_needed} boxes.')
