class CardValidator:
    def validator(self, card):
        erori = []
        if len(card.CNP) != 13:
            erori.append("CNP-ul trebuie sa aiba 13 cifre.")
        zi, luna, an = card.data_inregistrarii.split(".")
        if int(an) < 1900:
            erori.append("Nu este posibil sa avem un card mai vechi de 1900.")
        if int(luna) not in [1,2,3,4,5,6,7,8,9,10,11,12]:
            erori.append("Lunile sunt de la 1 la 12.")
        zi, luna, an = card.data_nasterii.split(".")
        if int(an) < 1900:
            erori.append("Nu exista persoane vii nascute mai devreme de 1900.")
        if int(luna) not in [1,2,3,4,5,6,7,8,9,10,11,12]:
            erori.append("Lunile sunt de la 1 la 12.")
        if len(erori) > 0:
            raise ValueError(erori)
