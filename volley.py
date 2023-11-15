from Volley.genepools import GenePool


class Manager:
    def __init__(self):
        self.super_genes = []
        self.names = []
        self.average_fitness = 0

    def add_super_genes(self, super_genes):
        for super_gene in super_genes:
            self.names.append(super_gene.name)
            self.super_genes.append(super_gene)

    def get_average_fitness(self):
        fitness_data = []
        for gene in self.super_genes:
            fitness_data.append(gene.fitness)

        self.average_fitness = sum(fitness_data) / len(fitness_data)
        return self.average_fitness


