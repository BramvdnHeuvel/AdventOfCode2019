def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

def manipulate(dic, cursor=0):
    value = dic[cursor]

    if value == 99:
        return [dic[i] for i in dic]
    
    c1 = dic[cursor+1]
    c2 = dic[cursor+2]
    c3 = dic[cursor+3]

    if value == 1:
        dic[c3] = dic[c1] + dic[c2]
    elif value == 2:
        dic[c3] = dic[c1] * dic[c2]
    else:
        print('Whoopsie!')
        return [dic[i] for i in dic]

    return manipulate(dic, cursor+4)

def calc_with_init_values(noun, verb):
    i = 0
    dic = {}

    for line in read_file('02/ex1/input.txt'):
        for num in line.split(','):
            dic[i] = int(num)
            i += 1
    
    dic[1] = noun
    dic[2] = verb

    return manipulate(dic)

if __name__ == '__main__':
    for i in range(100):
        for j in range(100):
            x = calc_with_init_values(i, j)
            if x[0] == 19690720:
                print(i, j)