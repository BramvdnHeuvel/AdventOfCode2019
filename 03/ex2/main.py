def read_file(file_name):
    with open(file_name, 'r') as reader:
        for line in reader:
            yield line.strip()

def walk_path(path_str):
    path = []
    x, y = 0, 0

    for arrow in path_str.split(','):
        direction = arrow[0]
        length = int(arrow[1:])

        for _ in range(length):
            if direction == 'U':
                x += 1
            elif direction == 'R':
                y += 1
            elif direction == 'D':
                x += -1
            elif direction == 'L':
                y += -1
            else:
                j = 1
                raise ValueError(f"Unknown direction type {direction}.")
            path.append((x, y))
    return path

def detect_closest_collision(path1, path2):
    closest = None

    for i, p in zip(range(len(path1)), path1):
        dist = i

        if closest is not None and closest < dist:
            continue

        if p not in path2:
            continue

        dist += path2.index(p)
        if closest is None:
            closest = dist
        closest = min(closest, dist)
    
    return closest+2

if __name__ == '__main__':
    paths = []
    for line in read_file('03/ex2/input.txt'):
        paths.append(walk_path(line))
    
    path1 = paths[0]
    path2 = paths[1]

    
    print(detect_closest_collision(path1, path2))