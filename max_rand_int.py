import random

def avg_rand_int(rand_ints):
    """ Takes an list of integers and returns their average. """
    i=0
    num_total = 0
    for num in rand_ints:
        num_total = num_total+num
        i = i + 1
    return (num_total/i)

def max_rand_int(rand_ints):
    i = 0
    max_int = 1
    for num in rand_ints:
        if (num > max_int):
            max_int = num

    return max_int

def count_odds(rand_ints):
    num_odds = 0
    for num in rand_ints:
        if (num % 2 == 1):
            num_odds = num_odds + 1
    return num_odds

def make_ints(how_many = 100):
    l=[]
    num = 1
    for i in range(how_many):
        num = random.randint(1,1000)
        l.append(num)
    return l

numbers = make_ints()
print(len(numbers))
print(sorted(numbers))
print(avg_rand_int(numbers))
print(max_rand_int(numbers))
print(count_odds(numbers))
