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

if __name__ == '__main__':
    dic = {}

    for string in read_file('06/ex1/input.txt'):
        dic[string.split(')')[1]] = Asteroid(string)
    
    print(inventarise(dic))
