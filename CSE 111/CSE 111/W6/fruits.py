def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    print(f'Reversed:{fruit_list.reverse()}')
    fruit_list.append('orange')
    
    print(f'append:{fruit_list}')
    index = fruit_list.index('apple')
    print(f" 'apple' is found at position {index} ")
    
    fruit_list.insert(index, 'cherry')
    print(f'Inserted: {fruit_list}')
    
    fruit_list.remove('banana')
    print(f'Removed: {fruit_list}')
    
    fruit_popped = fruit_list.pop
    print(f'Popped Fruit: {fruit_popped}')
    print(f'New list: {fruit_list}')
    
    fruit_list.sort()
    print(f'sorted: {fruit_list}')
    
    fruit_list.clear()
    print(f'cleared: {fruit_list}')
    
    main()
    