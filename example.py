from Volley.volley import Manager
from Volley.genepools import StringPool
from Volley.genetics import SuperGene as SG
from Volley.fitness import FitnessFunction


def fitness_function(data):
    data = [str(gene.data) for gene in data]
    data = "".join(data)

    target = "hello world"
    matches = sum(a == b for a, b in zip(target, data))

    score = matches / len(target)
    return score


pool = StringPool(1, "qwertyuiopasdfghjklzxcvbnm ")
manager = Manager()
a = SG(pool=pool, name="second", amount_genes=100)
b = SG(pool=pool, name="first", amount_genes=100)
c = SG(pool=pool, name="third", amount_genes=100)
d = SG(pool=pool, name="4", amount_genes=100)
e = SG(pool=pool, name="5", amount_genes=100)
f = SG(pool=pool, name="6", amount_genes=100)
g = SG(pool=pool, name="7", amount_genes=100)
h = SG(pool=pool, name="8", amount_genes=100)
i = SG(pool=pool, name="9", amount_genes=100)
j = SG(pool=pool, name="10", amount_genes=100)
k = SG(pool=pool, name="11", amount_genes=100)

function = FitnessFunction(function=fitness_function, super_genes=[a, b, c, d, e, f, g, h, i, j, k], start_kill=10, kill_percent_reduce=.2)

ii = i
for i in range(1000):
    score = function.fit()
    print("_________________: " ,i, " :_________________")
    print(score)
    print(a, b, c, d, e, f, g, h, i, j, k)

    if score >= .9:
        print(i)
        print(a, b, c, d, e, f, g, h, i, j, k)
        input("Stop:")
    function.shuffle_all()
print(a.get_best(), b.get_best(), c.get_best(), d.get_best(), e.get_best(), f.get_best(), g.get_best(), h.get_best(), ii.get_best(), j.get_best(), k.get_best())

function.plot()