def main():
    data = [
        ['Quinn','Briggs','435-689-0989',1234],
        ['Jason','Briggs','801-229-0231',1235],
        ['Christina','Briggs','208-123-3441',1236],
        ['Angie','Briggs','309-333-3241',1235],
        ['Alesha','Briggs','801-323-3441',1235],
        ['Jenette','Briggs','801-854-3211',1235]
    ]
    print(data)

    # Sort compound list by first name
    sort_key_finder = lambda mylist : mylist[2]
    new_list = sorted(data, key=sort_key_finder)
    print(new_list)

    # Make a list with Utah siblings only
    phone_number_checker = lambda item : item[2].startswith('801') or item[2].startswith('435')
    new_list = sorted(list(filter(phone_number_checker, data)), key=sort_key_finder)
    print(new_list)

    
if __name__ == '__main__':
    main()