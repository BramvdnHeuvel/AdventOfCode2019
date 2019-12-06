def calculate_fuel(weight):
    return int(weight/3) - 2

def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

if __name__ == '__main__':
    total = 0
    for l in read_file('01/ex1/input.txt'):
        total += calculate_fuel(int(l))
    
    print(total)