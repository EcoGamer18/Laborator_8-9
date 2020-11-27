import datetime
import random
import xlsxwriter

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

    def populatie(self, n):
        nume = ["Popescu", "Abaza", "Botescu", "Bogza", "Boteanu", "Costea",
                "Cupsa", "Danciu", "Cioaca", "Iaru", "Iacobescu", "Nistor",
                "Tiron", "Timofte", "Tescanu", "Xenopol", "Zaharescu"]
        prenume = ["Ada", "Eusebia", "Mihai", "Diana", "Delia", "Floarea", "Elvira",
                   "Floriana", "Evelina", "Eugenia", "Emilia", "Geta", "Lorena",
                   "Rebeca", "Profira", "Paulica", "Abel", "George", "Edgar", "Gelu",
                   "Felix", "Gabriel", "Ghita", "Jean", "Ovidiu"]
        for i in range(n):
            id = random.choice(range(1, 1000))
            while self.__card_client_repository.get_by_id(id) is not None:
                id = random.choice(range(1, 100))
            nume_ob = random.choice(nume)
            prenume_ob = random.choice(prenume)
            CNP = random.randint(10 ** 12, 10 ** 13 - 1)
            ziua = random.choice(range(1, 31))
            ziua_adaos = "0" if ziua <= 9 else ""
            luna = random.choice(range(1, 13))
            luna_adaos = "0" if luna <= 9 else ""
            anul = random.choice(range(1989, 2010))
            data_nasterii = ziua_adaos + str(ziua) + '.' + luna_adaos + str(luna) + '.' + str(anul)
            ziua = random.choice(range(1, 31))
            ziua_adaos = "0" if ziua <= 9 else ""
            luna = random.choice(range(1, 13))
            luna_adaos = "0" if luna <= 9 else ""
            anul = random.choice(range(anul+1, 2020))
            data_inregistrarii = ziua_adaos + str(ziua) + '.' + luna_adaos + str(luna) + '.' + str(anul)
            carduri = CardClient(id, nume_ob, prenume_ob, CNP, data_nasterii, data_inregistrarii)
            self.__card_client_repository.adaugare(carduri)

    def excel_carduri(self):
        carduri = self.__card_client_repository.get_all()
        workbook = xlsxwriter.Workbook('Carduri.xls')
        worksheet = workbook.add_worksheet()
        worksheet.set_column(1, 7, 15)
        bold = workbook.add_format({'bold': 1})
        worksheet.write('A1', 'Id card', bold)
        worksheet.write('B1', 'Nume', bold)
        worksheet.write('C1', 'Prenume', bold)
        worksheet.write('D1', 'CNP', bold)
        worksheet.write('E1', 'Data nasterii', bold)
        worksheet.write('F1', 'Data inregistrarii', bold)

        row = 1
        col = 0

        for card in carduri:
            worksheet.write_string(row, col, str(card.id_entitate))
            worksheet.write_string(row, col + 1, card.nume)
            worksheet.write_string(row, col + 2, card.prenume)
            worksheet.write_string(row, col + 3, str(card.CNP))
            worksheet.write_string(row, col + 4, card.data_nasterii)
            worksheet.write_string(row, col + 5, card.data_inregistrarii)
            row += 1

        workbook.close()
