class CardValidator:
    def validator(self,card):
        erori=[]
        zi,luna,an=card.data_inredistrarii.split(".")
        if an<1900:
            erori.append("Nu este posibil sa avem un card mai vechi de 1900.")
        zi, luna, an = card.data_nasterii.split(".")
        if an<1900:
            erori.append("Nu exista persoane vii nascute mai devreme de 1900.")
        if len(erori)>0:
            raise ValueError(erori)