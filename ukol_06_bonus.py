class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, stav_tachometru, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
        self.stav_tachometru = stav_tachometru
    
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici")

    def get_info(self):
        return f"registrační značka: {self.registracni_znacka}, typ: {self.typ_vozidla}, najeté kilometry: {self.najete_km}, dostupné: {self.dostupne}"


    def vrat_auto(self, stav_tachometru, dny_pujceni):
        self.stav_tachometru = stav_tachometru
        self.dostupne = True
        if dny_pujceni <= 7:
            cena = 400
        else:
            cena = 300
        cena_za_pujceni = cena * dny_pujceni
        return f"Cena za půjcení auta na {dny_pujceni} dnů je {cena_za_pujceni} Kč."

def najdi_auto(znacka, auta_pujcovny) -> Auto:
    """Metoda slouží k ověření, zda auto, které si chce uživatel půjčit, autopůčovna vlastní."""
    for auto in auta_pujcovny:
        if auto.typ_vozidla.startswith(znacka):
            return auto

    return None

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, 41253)

auta_pujcovny = [auto1, auto2]

# print(auto1.get_info())
# auto1.pujc_auto()
# print(auto1.get_info())

while True:
    pozadovana_znacka = input("Jakou značku auta si přejete půjčit? ")

    pozadovane_auto = najdi_auto(pozadovana_znacka, auta_pujcovny)
    if pozadovane_auto != None:
        print(pozadovane_auto.get_info())
        if pozadovane_auto.dostupne == True:
            pozadovane_auto.pujc_auto()
        else:
            print(f"Je nám líto, ale požadavané auto značky není momentálně k dispozici. Zvolte prosím jinou značku auta.")
    else:
        print(f"Je nám líto, ale požadavanou značku {pozadovana_znacka} nemáme. Můžete si vybrat značku Peugeot nebo Škoda.")
