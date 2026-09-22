# Programming Exercise 7-2

import random

def main():
    # Initialize list of numbers.
    number_list = [0] * 7

    # Assign random numbers to list.
    for i in range(7):
        number_list[i] = random.randint(0, 9)

    # Display numbers in a single line.
    # With square brackets
    print(number_list, sep=', ')
    # * = take the items out of the container and pass them individually (unpacking the list)
    print(*number_list, sep=', ')



# Call the main function.
if __name__ == '__main__':
    main()