import random


class System:
    def __init__(self, el_in_dim, dim):
        self.n = el_in_dim ** dim
        self.dim = dim
        self.el_in_dim = el_in_dim
        self.system = self.generate_system(el_in_dim, dim)

    @staticmethod
    def generate_system(l, dim):
        if dim == 1:
            return [random.choice([-1, 1]) for _ in range(l)]
        return [System.generate_system(l, dim - 1) for _ in range(l)]

    def simulate(self):

        def get_neighbours(coordinates):
            res = []
            for coord in range(len(coordinates)):
                state = coordinates[coord]
                if state + 1 < self.el_in_dim:
                    res.append(coordinates[:coord] + [state + 1] + coordinates[coord+1:])
                if state - 1 >= 0:
                    res.append(coordinates[:coord] + [state - 1] + coordinates[coord+1:])
            return res

        def increment_coord(ind):
            if current_coord[ind] + 1 == self.el_in_dim:
                current_coord[ind] = 0
                increment_coord(ind - 1)
            else:
                current_coord[ind] += 1

        current_coord = [0 for _ in range(self.dim)]
        modified = False

        for i in range(self.n):
            # print(current_coord)
            neighbours = [System.get(self.system, c) for c in get_neighbours(current_coord)]
            delta_u = 0
            current_state = System.get(self.system, current_coord)

            for state_operator in [1, -1]:
                current_state = state_operator * current_state
                for neighbour in neighbours:
                    delta_u += state_operator * (neighbour * current_state)

            if delta_u <= 0 or System.pdf():
                System.set(self.system, current_coord, current_state)
                modified = True

            increment_coord(len(current_coord) - 1)

        yield modified

    @staticmethod
    def get(system, coordinates):
        print(f'system: {system}')
        print(f'coords: {coordinates}')
        print(f'element: {system[coordinates[0]]}\n')
        if len(coordinates) == 1:
            return system[coordinates[0]]
        return System.get(system[coordinates[0]], coordinates[1:])

    @staticmethod
    def set(system, coordinates, value):
        if len(coordinates) == 1:
            system[coordinates[0]] = value
        else:
            System.set(system[coordinates[0]], coordinates[1:], value)

    @staticmethod
    def pdf():
        return random.choice([1, 0])

    def __str__(self):
        return str(self.system)
