from comms import OP_CODE

def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

def build_dict(file_name, init_input=0):
    i = 0
    dic = {'input': init_input}

    for line in read_file(file_name):
        for num in line.split(','):
            dic[i] = int(num)
            i += 1
    return dic

def build_params(dic, code, param_amount, cursor):
    def str_viewer(code):
        string = str(code)
        while len(string) < param_amount + 2:
            string = '0' + string
        
        for i in range(2, param_amount+2):
            yield int(string[len(string)-i-1])
    PARAM_TYPE = {
        0: 'position',
        1: 'immediate'
    }

    args = [dic, cursor]
    i = cursor + 1

    for c in str_viewer(code):
        args.append((dic[i], PARAM_TYPE[c]))
        i += 1
    return args

def evaluate_dict(dic, cursor=0):
    op_code = dic[cursor]
    comm = OP_CODE[op_code%100]

    args = build_params(dic, op_code, comm[1], cursor)
    
    try:
        new_cursor = comm[0](*args)
    except StopIteration:
        return None
    else:
        if new_cursor == None:
            return evaluate_dict(dic, cursor+comm[1]+1)
        else:
            return evaluate_dict(dic, new_cursor)

if __name__ == '__main__':
    dic = build_dict('input.txt', 5)
    x = evaluate_dict(dic)
    print(x)