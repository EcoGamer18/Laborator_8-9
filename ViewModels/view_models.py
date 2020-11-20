from Domain.card_client import CardClient
from Domain.masina import Masina


class ViewModels:
    def __init__(self, id_tranzactie, masina: Masina, suma_piese, suma_manopera, data, ora,
                 reducere_card, reducere_garantie):
        self.id_tranzactie = id_tranzactie
        self.masina = masina
        self.suma_piese = suma_piese
        self.suma_manopera = suma_manopera
        self.data = data
        self.ora = ora
        self.reducere_card = reducere_card
        self.reducere_garantie = reducere_garantie

    def __str__(self):
        suma_manopera_finala = self.suma_manopera * 9 / 10 if self.reducere_card is True else self.suma_manopera
        suma_piese_finala = 0 if self.reducere_garantie is True else self.suma_piese
        mesaj_reducere_piese = ''
        mesaj_reducere_manopera = ''
        if suma_piese_finala != self.suma_piese:
            mesaj_reducere_piese = " cu reducere datorita garantiei"
        if suma_manopera_finala != self.suma_manopera:
            if len(mesaj_reducere_piese) > 0:
                mesaj_reducere_manopera = " si"
            mesaj_reducere_manopera += " cu reducre datorita cardului"
        return f"Id-ul tranzactie: {self.id_tranzactie}\n-----------------\n" \
               f"cu masina:\n {self.masina}\n-----------\n are pretul initial" \
               f"{self.suma_piese + self.suma_manopera} si pretul final"
