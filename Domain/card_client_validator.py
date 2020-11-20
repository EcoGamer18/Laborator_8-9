import datetime

class CardValidator:
    def validator(self, card):
        erori = []
        today= datetime.date.today()
        try:
            id=int(card.id_entitate)
            if id<=0:
                raise ValueError
        except ValueError:
            erori.append("Id-ul trebuie sa fie de tipul int strict pozitiv.")
        if len(card.CNP) != 13:
            erori.append("CNP-ul trebuie sa aiba 13 cifre.")
        try:
            datetime.datetime.strptime(card.data_nasterii,'%d.%m.%Y')
        except ValueError:
            erori.append("Data nasterii trebuie sa fie formatul dd.mm.yyyy.")
        try:
            datetime.datetime.strptime(card.data_inregistrarii,'%d.%m.%Y')
        except ValueError:
            erori.append("Data inregistrarii trebuie sa fie formatul dd.mm.yyyy.")

        if len(erori) > 0:
            raise ValueError(erori)
