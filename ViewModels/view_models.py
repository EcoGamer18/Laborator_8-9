from Domain.masina import Masina


class ViewModels:
    def __init__(self, id_tranzactie, masina: Masina, suma_piese, suma_manopera, data, ora,
                 reducere_card, reducere_garantie, suma_piese_final, suma_manopera_final):
        self.id_tranzactie = id_tranzactie
        self.masina = masina
        self.suma_piese = suma_piese
        self.suma_manopera = suma_manopera
        self.data = data
        self.ora = ora
        self.reducere_card = reducere_card
        self.reducere_garantie = reducere_garantie
        self.suma_p_redusa = suma_piese_final
        self.suma_m_redusa = suma_manopera_final

    def __str__(self):
        mesaj_reducere_piese = ''
        mesaj_reducere_manopera = ''
        if self.suma_p_redusa != self.suma_piese:
            mesaj_reducere_piese = " cu reducere datorita garantiei"
        if self.suma_m_redusa != self.suma_manopera:
            if len(mesaj_reducere_piese) > 0:
                mesaj_reducere_manopera = " si"
            mesaj_reducere_manopera += " cu reducere datorita cardului"
        return f"Id-ul tranzactie: {self.id_tranzactie}\nde data de {self.data} la ora {self.ora}" \
               f"\n-----------------\n" \
               f"cu masina:\n{self.masina}\n-----------\nare pretul initial " \
               f"{self.suma_piese + self.suma_manopera} si pretul final " \
               f"{self.suma_m_redusa + self.suma_p_redusa}" + mesaj_reducere_piese + mesaj_reducere_manopera + ".\n"
