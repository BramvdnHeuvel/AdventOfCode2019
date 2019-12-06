def calculate_fuel(weight):
    return max(int(weight/3) - 2, 0)

def recursive_fuel(weight):
    fuel = calculate_fuel(weight)

    if fuel == 0:
        return 0
    return fuel + recursive_fuel(fuel)

def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

if __name__ == '__main__':
    total = 0
    for l in read_file('01/ex1/input.txt'):
        total += recursive_fuel(int(l))
    
    print(total)