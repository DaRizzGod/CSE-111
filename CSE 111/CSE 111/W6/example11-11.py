def main():
    numbers = [2, 3, 5, 1, 6]
    print(numbers)

    # Find the square of each number
    square_me = lambda number : number ** 2
    new_list = list(map(square_me, numbers))
    print(new_list)

    # List with Odd numbers only
    odd_only = lambda number : number % 2 == 1
    new_list = list(filter(odd_only, numbers))
    print(new_list)

    # Make a compound list with square and cube of each number
    make_square_cube = lambda number : [number ** 2, number ** 3]
    new_list = list(map(make_square_cube, numbers))
    print(new_list)  


if __name__ == '__main__':
    main()