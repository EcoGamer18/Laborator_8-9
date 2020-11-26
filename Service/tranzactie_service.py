from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Repository.file_repository import FileRepository
from ViewModels.view_models import ViewModels


class TranzactieService:
    def __init__(self, tranzactie_repository: FileRepository, masini_repository: FileRepository,
                 card_client_repository: FileRepository, tranzactie_validator: TranzactieValidator):
        self.__tranzactie_repository = tranzactie_repository
        self.__masini_repository = masini_repository
        self.__card_client_repository = card_client_repository
        self.__tranzactie_validator = tranzactie_validator

    def get_all(self):
        view_models = []
        for tranzactie in self.__tranzactie_repository.get_all():
            masina = self.__masini_repository.get_by_id(tranzactie.id_masina)
            view_models.append(
                ViewModels(tranzactie.id_entitate, masina, tranzactie.suma_piese, tranzactie.suma_manopera,
                           tranzactie.data, tranzactie.ora, tranzactie.reducere_card,
                           tranzactie.reducere_garantie, tranzactie.s_p_redusa, tranzactie.s_m_redusa))
        return view_models

    def adaugare(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        masina = self.__masini_repository.get_by_id(id_masina)
        card = self.__card_client_repository.get_by_id(id_card)
        reducere_card = False
        reducere_garantie = False
        if masina is None:
            raise KeyError("Nu se poate face tranzactia pentru ca nu exista masina cu id-ul dat.")
        if card is None and id_card != '0':
            raise KeyError("Nu se poate face tranzactia pentru ca nu exista card cu id-ul dat")
        if id_card != "0":
            reducere_card = True
        if masina.garantie == "DA":
            reducere_garantie = True
        suma_manopera_final = suma_manopera
        suma_piese_final = suma_piese
        if reducere_card:
            suma_manopera_final = 9 / 10 * suma_manopera
        if reducere_garantie:
            suma_piese_final = 0

        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora, reducere_card,
                                reducere_garantie, suma_piese_final, suma_manopera_final)
        self.__tranzactie_validator.validator(tranzactie)
        self.__tranzactie_repository.adaugare(tranzactie)

    def stergere(self, id_tranzactie):
        self.__tranzactie_repository.stergere(id_tranzactie)

    def modificare(self, id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora):
        tranzactie = self.__tranzactie_repository.get_by_id(id_tranzactie)

        if tranzactie is None:
            raise KeyError(f"Nu exista nicio comanda cu id-ul {id_tranzactie}")

        if id_masina != "":
            if self.__masini_repository.get_by_id(id_masina) is None:
                raise KeyError("Nu se poate modifica tranzactia pentru ca nu exista o masina cu id-ul dat")
            tranzactie.id_masina = id_masina
        if id_card != "":
            if self.__card_client_repository.get_by_id(id_card) is None and id_card != '0':
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

        masina = self.__masini_repository.get_by_id(tranzactie.id_masina)
        if id_card == "0":
            tranzactie.reducere_card = False
        if masina.garantie == "DA":
            tranzactie.reducere_garantie = True

        if tranzactie.reducere_card:
            tranzactie.s_m_redusa = 9 / 10 * tranzactie.suma_manopera
        if tranzactie.reducere_garantie:
            tranzactie.s_p_redusa = 0

        self.__tranzactie_validator.validator(tranzactie)
        self.__tranzactie_repository.modificare(tranzactie)

    def tranzactii_interval(self, inf, sup):
        tranzactii = self.__tranzactie_repository.get_all()
        tranzactii_interval = []
        for tranzactie in tranzactii:
            if inf <= tranzactie.s_p_redusa + tranzactie.s_m_redusa <= sup:
                masina = self.__masini_repository.get_by_id(tranzactie.id_masina)
                tranzactii_interval.append(
                    ViewModels(tranzactie.id_entitate, masina, tranzactie.suma_piese, tranzactie.suma_manopera,
                               tranzactie.data, tranzactie.ora, tranzactie.reducere_card,
                               tranzactie.reducere_garantie, tranzactie.s_p_redusa, tranzactie.s_m_redusa))
        return tranzactii_interval

    def masini_dupa_manopera(self):
        tranzactii = self.__tranzactie_repository.get_all()
        masini = self.__masini_repository.get_all()
        sortat = {}
        for tranzactie in tranzactii:
            if tranzactie.id_masina in sortat:
                sortat[tranzactie.id_masina] += tranzactie.s_m_redusa
            else:
                sortat[tranzactie.id_masina] = tranzactie.s_m_redusa
        masini_sortate = []
        chei = sortat.keys()

        for i in chei:
            masini_sortate.append([self.__masini_repository.get_by_id(i), sortat[i]])

        for masina in masini:
            if masina.id_entitate not in chei:
                masini_sortate.append([masina, 0])

        masini_sortate.sort(key=lambda x: x[1])

        return masini_sortate

    def carduri_dupa_valoarea_reducerii(self):
        tranzactii = self.__tranzactie_repository.get_all()
        carduri = self.__card_client_repository.get_all()

        sortat = {}

        for tranzactie in tranzactii:
            if tranzactie.id_card_client != '0':
                if tranzactie.id_card_client in sortat:
                    sortat[tranzactie.id_card_client] += tranzactie.suma_piese
                else:
                    sortat[tranzactie.id_card_client] = tranzactie.suma_piese

        carduri_sortate = []
        chei = sortat.keys()

        for i in chei:
            carduri_sortate.append([self.__card_client_repository.get_by_id(i), sortat[i]])

        for card in carduri:
            if card.id_entitate not in chei:
                carduri_sortate.append([card, 0])

        carduri_sortate.sort(key=lambda x: x[1] )

        return carduri_sortate
