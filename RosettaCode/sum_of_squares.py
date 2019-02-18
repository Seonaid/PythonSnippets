def sum_of_squares(num_list):
    total = 0
    print("num list = " + str(num_list))

    for num in num_list:
        total = total + num * num

    return total


