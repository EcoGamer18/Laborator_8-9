import datetime

from Domain.tranzactie import Tranzactie


class TranzactieValidator:
    def validator(self, tranzactie: Tranzactie):
        erori = []
        if tranzactie.suma_piese < 0:
            erori.append("Suma pieselor trebuie sa fie mai mare ca 0.")
        if tranzactie.suma_manopera < 0:
            erori.append("Suma manoperei trebuie sa fie mai mare ca 0.")
        try:
            datetime.datetime.strptime(tranzactie.data, '%d.%m.%Y')
        except ValueError:
            erori.append("Data trebuie sa fie formatul dd.mm.yyyy.")
        try:
            datetime.datetime.strptime(tranzactie.ora, '%H:%M')
        except ValueError:
            erori.append("Ora trebuie sa fie formatul hh:mm.")
        if len(erori)>0:
            raise ValueError(erori)
