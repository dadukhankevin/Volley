from Volley.volley import Manager
from Volley.genepools import StringPool
from Volley.genetics import SuperGene as SG
from Volley.fitness import FitnessFunction


def fitness_function(data):
    return data.count("a")


pool = StringPool(1, "qwertyuiopasdfghjklzxcvbnm")
manager = Manager()
a = SG(pool=pool, name="second", amount_genes=10)
b = SG(pool=pool, name="first", amount_genes=10)
c = SG(pool=pool, name="third", amount_genes=10)
d = SG(pool=pool, name="fourth", amount_genes=10)

function = FitnessFunction(function=fitness_function, super_genes=[a, b, c, d])

function.fit()
