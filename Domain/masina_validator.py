class MasinaValidator:
    def validator(self, masina):
        erori = []
        if masina.nr_km < 0:
            erori.append("Numarul de kilometrii facuti este strict mai mare ca 0.")
        if masina.anul_fabricatiei < 0:
            erori.append("Anul de fabricatie trebuie sa fie mai mare ca 0.")
        if masina.garantie is not "False" or masina.garantie is not "True":
            erori.append("Garantie poate avea doar valorile \"True\" sau \"False\"")
        if len(erori) > 0:
            raise ValueError(erori)
