import random

from Domain.card_client import CardClient
from Domain.card_client_validator import CardValidator
from Repository.file_repository import FileRepository


class CardClientService:
    def __init__(self, card_client_repository: FileRepository, card_client_validator: CardValidator):
        self.__card_client_repository = card_client_repository
        self.__card_client_validator = card_client_validator

    def get_all(self):
        return self.__card_client_repository.get_all()

    def adaugare(self, id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii):
        storage = self.__card_client_repository.get_all()
        for card in storage:
            if card.CNP == CNP:
                raise KeyError("CNP-ul dat apare si la alta persoana. CNP-ul trebuie sa fie unic.")
        card_client = CardClient(id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii)
        self.__card_client_validator.validator(card_client)
        self.__card_client_repository.adaugare(card_client)

    def stergere(self, id_card):
        self.__card_client_repository.stergere(id_card)

    def modificare(self, id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii):
        card_client = self.__card_client_repository.get_by_id(id_card)
        if card_client is None:
            raise KeyError(f"Nu exista cardul cu id-ul {id_card}")

        if nume != "":
            card_client.nume = nume
        if prenume != "":
            card_client.prenume = prenume
        if CNP != "":
            storage = self.__card_client_repository.get_all()
            for card in storage:
                if card.CNP == CNP:
                    raise KeyError("CNP-ul dat apare si la alta persoana. CNP-ul trebuie sa fie unic.")
            card_client.CNP = CNP
        if data_nasterii != "":
            card_client.data_nasterii = data_nasterii
        if data_inregistrarii != "":
            card_client.data_inregistrarii = data_inregistrarii

        self.__card_client_validator.validator(card_client)
        self.__card_client_repository.modificare(card_client)

    def populatie(self,n):
        nume=["Popescu","Abaza","Botescu","Bogza","Boteanu","Costea",
              "Cupsa","Danciu","Cioaca","Iaru","Iacobescu","Nistor",
              "Tiron","Timofte","Tescanu","Xenopol","Zaharescu"]
        prenume=["Ada","Eusebia","Mihai","Diana","Delia","Floarea","Elvira",
                 "Floriana","Evelina","Eugenia","Emilia","Geta","Lorena",
                 "Rebeca","Profira","Paulica","Abel","George","Edgar","Gelu",
                 "Felix","Gabriel","Ghita","Jean","Ovidiu"]
        for i in range(n):
            id= random.choice(range(1, 1000))
            while self.__card_client_repository.get_by_id(id) is not None:
                id = random.choice(range(1, 100))
            nume_ob=random.choice(nume)
            prenume_ob=random.choice(prenume)
            CNP=random.randint(10**12,10**13-1)
            ziua=random.choice(range(1,31))
            ziua_adaos= "0" if ziua<=9 else ""
            luna=random.choice(range(1,13))
            luna_adaos= "0" if luna<=9 else ""
            anul=random.choice(range(1989,2020))
            data_nasterii=ziua_adaos+str(ziua)+'.'+luna_adaos+str(luna)+'.'+str(anul)
            ziua = random.choice(range(1, 31))
            ziua_adaos = "0" if ziua <= 9 else ""
            luna = random.choice(range(1, 13))
            luna_adaos = "0" if luna <= 9 else ""
            anul = random.choice(range(1989, 2020))
            data_inregistrarii=ziua_adaos +str(ziua)+'.'+luna_adaos+str(luna)+'.'+str(anul)
            carduri=CardClient(id,nume_ob,prenume_ob,CNP,data_nasterii,data_inregistrarii)
            self.__card_client_repository.adaugare(carduri)





