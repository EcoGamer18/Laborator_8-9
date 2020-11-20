from Domain.tranzactie import Tranzactie
from Repository.file_repository import FileRepository


class TranzactieService:
    def __init__(self, tranzactie_repository: FileRepository, masini_repository: FileRepository,
                 card_client_repository: FileRepository):
        self.__tranzactie_repository = tranzactie_repository
        self.__masini_repository = masini_repository
        self.__card_client_repository = card_client_repository

    def get_all(self):
        pass

    def adaugare(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        masina = self.__masini_repository.get_by_id(id_masina)
        card = self.__card_client_repository.get_by_id(id_card)

        if masina is None:
            raise KeyError("Nu se poate face tranzactia pentru ca nu exista masina cu id-ul dat.")
        if card is None:
            raise KeyError("Nu se poate face tranzactia pentru ca nu exista card cu id-ul dat")
        if id_card == "0":
            reducere_card = False
        if masina.garantie is "True":
            reducere_garantie = True

        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora, reducere_card,
                                reducere_garantie)

        self.__tranzactie_repository.adaugare(tranzactie)

    def stergere(self, id_tranzactie):
        self.__tranzactie_repository.stergere(id_tranzactie)

    def modificare(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        tranzactie = self.__tranzactie_repository.get_by_id(id_tranzactie)

        if tranzactie is None:
            raise KeyError(f"Nu exista nicio comanda cu id-ul {id_comanda}")

        if id_masina != "":
            if self.__masini_repository.get_by_id(id_masina) is None:
                raise KeyError("Nu se poate modifica tranzactia pentru ca nu exista o masina cu id-ul dat")
            tranzactie.id_masina = id_masina
        if id_card != "":
            if self.__card_client_repository.get_by_id(id_card) is None:
                raise KeyError("Nu se poate modifica tranzactia pentru ca nu exista un card client cu id-ul dat")
            tranzactie.id_card = id_card
        if suma_piese != 0:
            tranzactie.suma_piese = suma_piese
        if suma_manopera != 0:
            tranzactie.suma_manopera = suma_manopera
        if data != "":
            tranzactie.data = data
        if ora != "":
            tranzactie.ora = ora

        masina = self.__masini_repository.get_by_id(id_masina)
        if id_card == "0":
            tranzactie.reducere_card = False
        if masina.garantie is "True":
            tranzactie.reducere_garantie = True

        self.__tranzactie_repository.modificare(tranzactie)
