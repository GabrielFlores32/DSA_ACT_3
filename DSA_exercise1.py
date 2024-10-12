def square_of_odds():
    int_list = list(range(1, 21))  
    #List only include squares of odd numbers
    return [x ** 2 for x in int_list if x % 2 != 0]

#Print the square of the odd int
print("Square of odd numbers from 1 to 20:", square_of_odds())