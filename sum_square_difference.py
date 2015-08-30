def sum_square_difference(limit):
    sum_square = 0
    square_sum = 0
    for i in range(1, limit+1):
        sum_square += i ** 2
        square_sum += i
    square_sum **= 2
    print square_sum - sum_square

sum_square_difference(100)