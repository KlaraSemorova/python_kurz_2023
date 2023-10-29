import math

def platne_cislo(telefonni_cislo: str) -> bool:
    """"Funkce ověřuje, zda uživatel zadal tel. číslo ve správném formátu, tj. jestli je číslo 9místné nebo 13 místné s předvolbou +420."""
    tel_cislo = telefonni_cislo.replace(" ", "")
    delka_cisla = len(tel_cislo)
    if delka_cisla == 9 or (delka_cisla == 13 and tel_cislo[0:4] == "+420"):
        return True
    else:
        return False

def cena_zpravy(zprava: str, cena: int = 3) -> int:
    """Funkce počítá cenu zprávy, kdy za každých započatých 180 znaků je cena 3 Kč"""
    delka_zpravy = len(zprava)
    celkova_cena = math.ceil(delka_zpravy / 180) * cena
    return celkova_cena

cislo = (input("Zadejte telefonní číslo: "))

if platne_cislo(cislo) == True:
   text = input("Napište text: ")
   print(f"Za zprávu na telefonní číslo {cislo} zaplatíte {cena_zpravy(text)} Kč.")
else:
    print("Zadané číslo není ve správném formátu.")