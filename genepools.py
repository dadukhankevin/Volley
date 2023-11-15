import numpy as np
from typing import Union
from Volley.genetics import SuperGene, Gene


class GenePool:
    def __init__(self, amount: int):
        self.amount = amount

    def generate_genes(self, manager, name: str, n: int):
        pass


class StringPool(GenePool):
    def __init__(self, amount, alphabet: Union[np.ndarray, list, str], replacement: bool = True):
        super().__init__(amount)
        self.replacement = replacement
        if type(alphabet) == str:
            self.alphabet = np.asarray(list(alphabet))
        else:
            self.alphabet = np.asarray(alphabet)

    def generate_super(self, name: str, amount_genes: int):
        return SuperGene(self, name=name, amount_genes=amount_genes)

    def generate_genes(self, super_gene, name: str, n: int):
        genes = []
        for i in range(n):
            genes.append(Gene(np.random.choice(self.alphabet, self.amount, self.replacement), super_gene, name + str(i)))
        return genes
