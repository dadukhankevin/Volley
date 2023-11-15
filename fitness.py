from Volley.genetics import SuperGene


class FitnessFunction:
    def __init__(self, function, super_genes: list[SuperGene]):
        self.function = function
        self.super_genes = super_genes

    def fit(self):
        fitness = self.function(self.super_genes)
        for super_gene in self.super_genes:
            super_gene.current_gene.fit(fitness)
        return fitness

    def shuffle_all(self):
        for gene in self.super_genes:
            gene.shuffle()

    def get_average_fitness(self):
        fitness_data = []
        for gene in self.data:
            fitness_data.append(gene.fitness)
        self.average_fitness = sum(fitness_data) / len(fitness_data)
        return self.average_fitness
