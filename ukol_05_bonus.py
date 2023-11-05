teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

# řešení 1
def prumer(den):
    return sum(den[1:])/len(den[1:])

slovnik_prumerne_teplota = {den[0]: prumer(den) for den in teploty}
print(slovnik_prumerne_teplota)

# řešení 2
slovnik_teploty = {den[0]: den[1:] for den in teploty}
# print(slovnik_teploty)

def prumer(den):
    """Funkce pocita prumer"""
    return sum(den)/len(den)

slovnik_prumerna_teploty = {den: prumer(teplota) for den, teplota in slovnik_teploty.items()}
print(slovnik_prumerna_teploty)