import random


class System:
    def __init__(self, l, dim):
        self.n = l ** dim
        self.dim = dim
        self.l = l
        self.system = self.generate_system(l, dim)

    @staticmethod
    def generate_system(l, dim):
        if dim == 1:
            return [random.choice([-1, 1]) for _ in range(l)]
        return [System.generate_system(l, dim - 1) for _ in range(l)]

    def simulate(self):
        def get_neighbours(coords):
            res = []
            for coord in range(len(coords)):
                state = coords[coord]
                if state + 1 < len(coords):
                    res.append(coords[:coord] + [state + 1] + coords[coord+1:])
                if state - 1 >= 0:
                    res.append(coords[:coord] + [state - 1] + coords[coord+1:])
            return res

        current_coord = [0 for _ in range(self.dim)]

        def increment_coord(ind):
            if current_coord[ind] + 1 == self.l:
                current_coord[ind] = 0
                increment_coord(ind - 1)
            else:
                current_coord[ind] += 1

        for i in range(self.n):
            increment_coord(len(current_coord) - 1)
            neighbours = [System.get(self.system, c) for c in get_neighbours(current_coord)]

            sum = 0
            current_state = System.get(self.system, current_coord)
            for state in [-1, 1]:
                current_state = -1 * state * current_state
                for neighbour in neighbours:
                    sum += state * (neighbour * current_state * -1)

            if sum <= 0 or System.pdf():
                System.set(self.system, current_coord, current_state)

    @staticmethod
    def get(system, coords):
        if len(coords) == 1:
            return system[coords[0]]
        return get(system[coords[0], coords[1:]])

    @staticmethod
    def set(system, coords, value):
        if len(coords) == 1:
            system[coords[0]] = value
        get(system[coords[0], coords[1:]])

    @staticmethod
    def pdf():
        return random.choice([1, 0])

    def __str__(self):
        return str(self.system)


if __name__ == '__main__':
    DIMENSIONS = 3
    L = 2

    system = System(L, DIMENSIONS)

    print(system)

    system.simulate()
