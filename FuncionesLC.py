# Función del ejemplo zip
def lz(x, y, z):
    la = (x, y, z)
    return list(la)


c_1 = ["a", "b", "c"]
c_2 = ["1", "2", "3"]
c_3 = ["d", "e", "f"]
a = lz(c_1, c_2, c_3)
print(a)


# Función del ciclo for

def cf(x, n):
    lcf = [i + n for i in x]
    return lcf


l_cf = [1, 2, 3, 4, 5, 6]
n = 5
d = cf(l_cf, n)
print(d)


# Función de la condicional if

def ci(x):
    lci = [i for i in x if i % 2 == 0]
    return lci


li1 = [1, 2, 4, 6, 5, 8, 3, 2]
e = ci(li1)
print(e)

# Finción de la condicional  if-else
import random


def ce(x, y):
    li = [i if random.random() >= 0.5 else j for i, j in zip(x, y)]
    return li


le1 = [1, 2, 3, 4, 5]
le2 = [6, 7, 8, 9, 10]
d = ce(le1, le2)
print(d)