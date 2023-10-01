jmeno = "Klara"
email = jmeno + "@czechitas.cz"
print(email)


# bonus
jmeno_a_prijmeni = input("Zadej svoje jméno a příjmení: ")

# všechna velká
print(jmeno_a_prijmeni.upper())

# všechna malá
print(jmeno_a_prijmeni.lower())

# první písmena jména a příjmení velká
jmena = jmeno_a_prijmeni.split(" ")
cele_jmeno = ""
for i, jmeno in enumerate(jmena):
    transformovano_jedno_slovo = jmeno.upper()[0] + jmeno.lower()[1:]
    if i > 0:
        cele_jmeno = cele_jmeno + " " + transformovano_jedno_slovo
    else:
        cele_jmeno = cele_jmeno + transformovano_jedno_slovo

print(cele_jmeno)

# vypsat iniciály
jmena = jmeno_a_prijmeni.split(" ")
cele_jmeno = ""
for i, jmeno in enumerate(jmena):
    transformovano_jedno_slovo = jmeno.upper()[0]
    if i > 0:
        cele_jmeno = cele_jmeno + ". " + transformovano_jedno_slovo + "."
    else:
        cele_jmeno = cele_jmeno + transformovano_jedno_slovo

print(cele_jmeno)


# křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá
