from Volley.genetics import SuperGene
import matplotlib.pyplot as plt

class FitnessFunction:
    def __init__(self, function, super_genes: list[SuperGene], start_kill=1, kill_percent_reduce = .1):
        self.start_kill = start_kill
        self.function = function
        self.super_genes = super_genes
        self.kill_percent_reduce = kill_percent_reduce
        self.epoch = 0
        self.history = []

    def fit(self):
        data = [super_gene.current_gene for super_gene in self.super_genes]
        fitness = self.function(data)
        self.history.append(fitness)
        self.epoch += 1
        for super_gene in self.super_genes:
            super_gene.current_gene.fit(fitness)
        if self.epoch >= self.start_kill:
            for super_gene in self.super_genes:
                super_gene.check(self.kill_percent_reduce)
        return fitness

    def shuffle_all(self):
        for gene in self.super_genes:
            gene.shuffle()

    def plot(self):
        plt.plot(self.history)
        plt.show()

