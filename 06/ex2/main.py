def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

class Asteroid:
    def __init__(self, string):
        self.name = string.split(')')[1]
        self.orbits = string.split(')')[0]

        self.orbitees = []
    
    def count_sub_orbits(self, i):
        return sum([orb.count_sub_orbits(i+1) for orb in self.orbitees]) + i

def inventarise(dic):
    com = Asteroid('NO-ONE)COM')

    for orb in dic:
        asteroid = dic[orb]

        if asteroid.orbits == 'COM':
            com.orbitees.append(asteroid)
        else:
            dic[asteroid.orbits].orbitees.append(asteroid)
    
    return com.count_sub_orbits(0)

def get_path_to(dic, destination):
    path = []

    asteroid = dic[destination]
    while asteroid.orbits != 'COM':
        path.append(asteroid.name)
        asteroid = dic[asteroid.orbits]
    path.append('COM')
    
    path.reverse()
    return path

if __name__ == '__main__':
    dic = {}

    for string in read_file('06/ex2/input.txt'):
        dic[string.split(')')[1]] = Asteroid(string)
    
    inventarise(dic)

    you = get_path_to(dic, 'YOU')
    san = get_path_to(dic, 'SAN')

    total = len(you) + len(san)

    for y, s, i in zip(you, san, range(total)):
        if y != s:
            print(total - 2*i -2)
            break