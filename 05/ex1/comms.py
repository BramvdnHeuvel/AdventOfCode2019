def look_up(dic, param):
    if param[1] == 'position':
        return dic[param[0]]
    elif param[1] == 'immediate':
        return param[0]
    else:
        raise ValueError("Unknown paramter type.")

# ----------------------------------------->

def add(dic, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    dic[param3[0]] = p1 + p2

def multiply(dic, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    dic[param3[0]] = p1 * p2

def get_input(dic, param1):
    dic[param1[0]] = dic['input']

def output(dic, param1):
    print(dic[param1[0]])

def finish(dic):
    raise StopIteration("Encountered code 99.")

# ----------------------------------------->

OP_CODE = {
    1: (add, 3),
    2: (multiply, 3),
    3: (get_input, 1),
    4: (output, 1),
    99: (finish, 0)
}