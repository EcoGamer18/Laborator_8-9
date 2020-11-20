from Domain.entitate import Entitate


class Tranzactie(Entitate):
    def __init__(self, id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera, data, ora, reducere_card,
                 reducere_garantie):
        super().__init__(id_tranzactie)
        self.__id_masina = id_masina
        self.__id_card_client = id_card_client
        self.__suma_piese = suma_piese
        self.__suma_manopera = suma_manopera
        self.__data = data
        self.__ora = ora
        self.__reducere_card = reducere_card
        self.__reducere_garantie = reducere_garantie

    @property
    def id_masina(self):
        return self.__id_masina

    @id_masina.setter
    def id_masina(self, id_masina_nou):
        self.__id_masina = id_masina_nou

    @property
    def id_card_client(self):
        return self.__id_card_client

    @id_card_client.setter
    def id_card_client(self, id_card_client_nou):
        self.__id_card_client = id_card_client_nou

    @property
    def suma_piese(self):
        return self.__suma_piese

    @suma_piese.setter
    def suma_piese(self, suma_piese_noua):
        self.__suma_piese = suma_piese_noua

    @property
    def suma_manopera(self):
        return self.__suma_manopera

    @suma_manopera.setter
    def suma_manopera(self, suma_manopera_noua):
        self.suma_manopera = suma_manopera_noua

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_noua):
        self.__data = data_noua

    @property
    def ora(self):
        return self.__ora

    @ora.setter
    def ora(self, ora_noua):
        self.__ora = ora_noua

    @property
    def reducere_card(self):
        return self.__reducere_card

    @reducere_card.setter
    def reducere_card(self, reducere_card_noua):
        self.__reducere_card = reducere_card_noua

    @property
    def reducere_garantie(self):
        return self.__reducere_garantie

    @reducere_garantie.setter
    def reducere_garantie(self, reducere_garantie_noua):
        self.__reducere_garantie = reducere_garantie_noua
