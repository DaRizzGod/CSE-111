def main():
    fruits = ['peach','pear','apple','plum','banana']
    print(fruits)

    # Capitalize these fruits
    capitalize_me = lambda fruit : fruit.capitalize()
    new_list = list(map(capitalize_me, fruits))
    print(new_list)

    # Make Plurals from the fruits
    pluralizer = lambda fruit : 'peaches' if fruit == 'peach' else fruit + 's'
    new_list = list(map(pluralizer, fruits))
    print(new_list)

    # Return a list of only "p" fruits
    p_fruits = lambda fruit : fruit.lower().startswith('p')
    new_list = list(filter(p_fruits, fruits))
    print(new_list)

def pluralizer2(fruit):
    if fruit == 'peach':
        return 'peaches'
    else:
        return fruit + 's'


if __name__ == '__main__':
    main()