import numpy as np
from typing import Union
from Volley.genetics import Gene


class GenePool:
    def __init__(self, amount: int):
        self.amount = amount

    def generate(self):
        pass


class StringPool(GenePool):
    def __init__(self, amount, alphabet: Union[np.ndarray, list, str], replacement: bool = True):
        super().__init__(amount)
        self.replacement = replacement
        if type(alphabet) == str:
            self.alphabet = np.asarray(list(alphabet))
        else:
            self.alphabet = np.asarray(alphabet)

    def generate(self, manager, name):
        return Gene(np.random.choice(self.alphabet, self.amount, self.replacement), manager=manager, name=name)
