class MasinaValidator:
    def validator(self,masina):
        erori=[]
        if masina.nr_km <0 :
            erori.append("Numarul de km este mai mare strict ca 0.")
        if masina.an_achizitie <0:
            erori.append("Anul de achizitie nu poate fi mai mic decat 1.")
        if len(erori)>0:
            raise ValueError(erori)