from numpy import np
from Volley.volley import Manager


def update_mean(current_mean, n, new_value):
    new_mean = (current_mean * n + new_value) / (n + 1)
    return new_mean


class Gene:
    def __init__(self, data: np.array, manager: Manager, name: str):
        self.data = data
        self.manager = manager
        self.total = 1
        self.fitness = 1

    def fit(self, fitness):
        self.fitness = update_mean(self.fitness, self.total, fitness)
        self.total += 1

    def check(self):
        if self.fitness < self.manager.average_fitness:
            self.kill()
        else:
            pass

    def kill(self):
        self.manager.genes.remove(self)

    def __str__(self):
        return str(self.data)

    def __float__(self):
        return self.fitness

    def __add__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data + other.data, self.manager, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data + np.array(other), self.manager, "result")
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data - other.data, self.manager, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data - np.array(other), self.manager, "result")
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data * other.data, self.manager, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data * np.array(other), self.manager, "result")
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data / other.data, self.manager, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data / np.array(other), self.manager, "result")
        else:
            return NotImplemented

    def __getitem__(self, index):
        return self.data[index]
