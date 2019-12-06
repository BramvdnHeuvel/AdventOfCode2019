INPUT_MIN = '359282'
INPUT_MAX = '820401'

def make_number(curr_str=''):
    l = len(curr_str)

    if l > 0:
        min, max = int(INPUT_MIN[0:l]), int(INPUT_MAX[0:l])
        if int(curr_str) < min or int(curr_str) > max:
            return 0
    
    total = 0

    if l == 0:
        for i in range(int(INPUT_MIN[0]), int(INPUT_MAX[0])+1):
            total += make_number(str(i))
    elif l < 6:
        for i in range(int(curr_str[-1]), 10):
            total += make_number(curr_str+str(i))
    else:
        total = contains_double(curr_str)
    
    return total

def contains_double(string):
    for i in range(5):
        if string[i] == string[i+1]:
            return 1
    return 0

if __name__ == '__main__':
    print(make_number())