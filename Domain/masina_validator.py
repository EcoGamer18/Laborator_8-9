class MasinaValidator:
    def validator(self, masina):
        erori = []
        if masina.nr_km < 0:
            erori.append("Numarul de kilometrii facuti este strict mai mare ca 0.")
        if masina.an_achizitie < 0:
            erori.append("Anul de fabricatie trebuie sa fie mai mare ca 0.")
        if masina.garantie != "False" or masina.garantie != "True":
            erori.append("Garantie poate avea doar valorile \"True\" sau \"False\"")
        if len(erori) > 0:
            raise ValueError(erori)
