
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# prumerne teploty pro každý den
def prumer(den):
    return sum(den)/len(den)

prumerne_teploty = [prumer(dny) for dny in teploty]
print(prumerne_teploty)

# ranní teploty
ranni_teploty = [dny[0] for dny in teploty]
print(ranni_teploty)

# ranní teploty
vecerni_teploty = [dny[2] for dny in teploty]
print(vecerni_teploty)

# ranní teploty
def poledne_noc(den):
    return [den[1], den[3]]

poledni_nocni_teploty = [poledne_noc(dny) for dny in teploty]
print(poledni_nocni_teploty)