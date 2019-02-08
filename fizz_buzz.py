def make_response(num):
    if (num % 15 == 0):
        return'fizz_buzz'
    elif (num % 5 == 0):
        return 'buzz'
    elif (num % 3 == 0):
        return'fizz'
    else:
        return num  


def fizz_buzz(*args):
    send_back = {}
    
    if (len(args) == 0):
        for i in range(1,101):
            if (make_response(i) != ''):
                send_back[i] = make_response(i)
    else:
        for arg in args:
            if (type(arg) == list):
               return 'sent list'
            elif (type(arg) == int):
                send_back[arg] = make_response(arg)

    return send_back

print(fizz_buzz(3, 6, 2, 0, 15, 7, 8))