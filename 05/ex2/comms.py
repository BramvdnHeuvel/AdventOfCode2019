def look_up(dic, param):
    if param[1] == 'position':
        return dic[param[0]]
    elif param[1] == 'immediate':
        return param[0]
    else:
        raise ValueError("Unknown paramter type.")

# ----------------------------------------->

def add(dic, cursor, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    dic[param3[0]] = p1 + p2
    return None

def multiply(dic, cursor, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    dic[param3[0]] = p1 * p2
    return None

def get_input(dic, cursor, param1):
    dic[param1[0]] = dic['input']
    return None

def output(dic, cursor, param1):
    print(dic[param1[0]])
    return None

def jump_if_true(dic, cursor, param1, param2):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    if p1 != 0:
        return p2
    else:
        return None
    
def jump_if_false(dic, cursor, param1, param2):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    if p1 == 0:
        return p2
    else:
        return None

def less_than(dic, cursor, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    if p1 < p2:
        dic[param3[0]] = 1
    else:
        dic[param3[0]] = 0
    return None

def equals(dic, cursor, param1, param2, param3):
    p1 = look_up(dic, param1)
    p2 = look_up(dic, param2)

    if p1 == p2:
        dic[param3[0]] = 1
    else:
        dic[param3[0]] = 0
    return None

def finish(dic, cursor):
    raise StopIteration("Encountered code 99.")

# ----------------------------------------->

OP_CODE = {
    1: (add, 3),
    2: (multiply, 3),
    3: (get_input, 1),
    4: (output, 1),
    5: (jump_if_true, 2),
    6: (jump_if_false, 2),
    7: (less_than, 3),
    8: (equals, 3),
    99: (finish, 0)
}