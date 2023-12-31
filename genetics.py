import random

import numpy as np


def update_mean(current_mean, n, new_value):
    new_mean = (current_mean * n + new_value) / (n + 1)

    return new_mean


class Gene:
    def __init__(self, data: np.array, super_gene, name: str):
        self.data = data
        self.super_gene = super_gene
        self.total = 1
        self.fitness = 1
        self.name = name

    def fit(self, fitness):
        self.fitness += fitness
        self.total += 1

    def check(self, percent=.1):
        if self.fitness < (self.super_gene.average_fitness * (1 - percent)):
            self.kill()
        else:
            pass

    def kill(self):
        self.data = self.super_gene.pool.generate_genes(self.super_gene, self.name, 1)[0].data

    def __str__(self):
        return str(self.data)

    def __float__(self):
        return self.fitness

    def __add__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data + other.data, self.super_gene, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data + np.array(other), self.super_gene, "result")
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data - other.data, self.super_gene, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data - np.array(other), self.super_gene, "result")
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data * other.data, self.super_gene, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data * np.array(other), self.super_gene, "result")
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Gene):
            return Gene(self.data / other.data, self.super_gene, "result")
        elif isinstance(other, (list, np.ndarray)):
            return Gene(self.data / np.array(other), self.super_gene, "result")
        else:
            return NotImplemented

    def __getitem__(self, index):
        return self.data[index]


class SuperGene(Gene):
    def __init__(self, pool, name: str, amount_genes):
        super().__init__(data=pool.generate_genes(self, name, amount_genes), super_gene=self, name=name)
        self.average_fitness = 1
        self.p = np.ones(amount_genes).tolist()
        self.pool = pool
        self.current_gene = self.data[0]  # TODO: randomize this

    def get_average_fitness(self):
        fitness_data = []
        self.p = []
        for gene in self.data:
            fitness_data.append(gene.fitness)
            self.p.append(gene.fitness)
        self.average_fitness = sum(fitness_data) / len(fitness_data)
        return self.average_fitness

    def shuffle(self):
        self.get_average_fitness()
        self.current_gene = random.choice(self.data)#, #weights=self.p, k=1)[0]

    def get_best(self):
        index = self.p.index(max(self.p))
        return self.data[index]

    def check(self, percent=.1):
        for gene in self.data:
            gene.check(percent)

    def __add__(self, other):
        return self.current_gene.__add__(other)

    def __mul__(self, other):
        return self.current_gene.__mul__(other)

    def __getitem__(self, index):
        return self.current_gene.__getitem__(index)

    def __str__(self):
        return self.current_gene.__str__()

    def __int__(self):
        return self.current_gene.__int__()

    def __float__(self):
        return self.current_gene.__float__()
