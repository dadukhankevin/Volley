from Volley.genepools import GenePool


class Manager:
    def __init__(self):
        self.genes = []
        self.average_fitness = 0

    def add_gene(self, genepool: GenePool):
        self.genes.append(genepool.generate(self))

    def get_average_fitness(self):
        fitness_data = []
        for gene in self.genes:
            fitness_data.append(gene.fitness)

        self.average_fitness = sum(fitness_data) / len(fitness_data)
        return self.average_fitness
