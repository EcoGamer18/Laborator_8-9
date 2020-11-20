from Service.card_client_service import CardClientService
from Service.masina_service import MasinaService
from Service.tranzactie_service import TranzactieService
from simple_colors import yellow, red


class Consola:
    def __init__(self, masina_service: MasinaService, card_client_service: CardClientService,
                 tranzactie_service: TranzactieService):
        self.__masina_service = masina_service
        self.__card_client_service = card_client_service
        self.__tranzactie_service = tranzactie_service

    def run_menu(self):
        while True:
            print("1.CRUD masini\n"
                  "2.CRUD carduri\n"
                  "3.CRUD tranzactii\n"
                  "x.Iesire")
            option = input("Alegeti o optiune:\n")
            if option == '1':
                self.run_crud_masini()
            elif option == '2':
                self.run_crud_carduri()
            elif option == '3':
                self.run_crud_tranzactii()
            elif option == 'x':
                break
            else:
                print("Optiune invalida")

    def run_crud_masini(self):
        while True:
            print("1.Adaugare masina\n"
                  "2.Stergere masina\n"
                  "3.Modificare masina\n"
                  "a.Afiseaza toate masinile\n"
                  "x.Iesire din meniul \"CRUD masini\"\n")
            option = input("Alegeti optiunile:\n")
            if option == '1':
                self.ui_adaugare_masina()
            elif option == '2':
                self.ui_stergere_masina()
            elif option == '3':
                self.ui_modificare_masina()
            elif option == 'a':
                self.ui_afisare_masini()
            elif option == 'x':
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_masina(self):
        try:
            id_masina = input("Id-ul masinii: ")
            model = input("Modelul masinii: ")
            an_achizitie = int(input("Anul achizitiei(>0): "))
            nr_km = int(input("Numarul de km(>0): "))
            garantie = input("Garantie (DA/NU): ")

            self.__masina_service.adaugare(id_masina, model, an_achizitie, nr_km, garantie)
            print(yellow("Masina a fost adaugata.", ['italic']))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_masina(self):
        try:
            id_masina = input("Dati Id-ul masinii pe care vreti sa o stergeti: ")

            self.__masina_service.stergere(id_masina)
            print(yellow("Masina a fost stearsa.", ['italic']))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_masina(self):
        try:
            id_masina = input("Id-ul masinii de modificat: ")
            model = input("Modelul nou al  masinii sau nimic daca vreti sa ramana la fel: ")
            an_achizitie = int(input("Anul nou al achizitiei (>0) sau 0 daca vreti sa ramana la fel: "))
            nr_km = int(input("Numarul nou de km (>0) sau 0 daca vreti sa ramana la fel: "))
            garantie = input("Garantie (DA/NU) sau nimic daca vreti sa ramana la fel: ")

            self.__masina_service.modificare(id_masina, model, an_achizitie, nr_km, garantie)
            print(yellow("Masina a fost modificata.", ['italic']))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_masini(self):
        masini = self.__masina_service.get_all()
        for masina in masini:
            print(masina)

    def run_crud_carduri(self):
        while True:
            print("1.Adaugare card\n"
                  "2.Stergere card\n"
                  "3.Modificare card\n"
                  "a.Afiseaza toate cardurile\n"
                  "x.Iesire din meniul \"CRUD carduri\"\n")
            option = input("Alegeti optiunile:\n")
            if option == '1':
                self.ui_adaugare_card()
            elif option == '2':
                self.ui_stergere_card()
            elif option == '3':
                self.ui_modificare_card()
            elif option == 'a':
                self.ui_afisare_carduri()
            elif option == 'x':
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_card(self):
        # try:
        id_card = input("Id-ul cardului: ")
        nume = input("Numele clientului: ")
        prenume = input("Prenumele clientului: ")
        CNP = input("CNP-ul clientului: ")
        data_nasterii = input("Data nasterii clientului(dd.mm.yyyy): ")
        data_inregistrarii = input("Data inregistrarii(dd.mm.yyyy): ")

        self.__card_client_service.adaugare(id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii)
        '''except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)'''

    def ui_stergere_card(self):
        try:
            id_card = input("Dati Id-ul cardului pe care vreti sa il stergeti: ")

            self.__card_client_service.stergere(id_card)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_card(self):
        try:
            id_card = input("Id-ul cardului pe care vreti sa il modificati: ")
            nume = input("Numele nou al clientului sau nimic daca nu doriti sa il modificati: ")
            prenume = input("Prenumele nou al clientului sau nimic daca nu doriti sa il modificati: ")
            CNP = input("CNP-ul nou al clientului sau nimic daca nu doriti sa il modificati: ")
            data_nasterii = input(
                "Data nasterii noua a clientului (dd.mm.yyyy) sau nimic daca nu doriti sa il modificati: ")
            data_inregistrarii = input(
                "Data noua a inregistrarii (dd.mm.yyyy) sau nimic daca nu doriti sa il modificati: ")

            self.__card_client_service.modificare(id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_carduri(self):
        carduri = self.__card_client_service.get_all()
        for card in carduri:
            print(card)

    def run_crud_tranzactii(self):
        while True:
            print("1.Adaugare tranzactie\n"
                  "2.Stergere tranzactie\n"
                  "3.Modificare tranzactie\n"
                  "a.Afiseaza toate tranzactiile\n"
                  "x.Iesire din meniul \"CRUD tranzactii\"\n")
            option = input("Alegeti optiunile:\n")
            if option == '1':
                self.ui_adaugare_tranzactie()
            elif option == '2':
                self.ui_stergere_tranzactie()
            elif option == '3':
                self.ui_modificare_tranzactie()
            elif option == 'a':
                self.ui_afisare_tranzactii()
            elif option == 'x':
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_tranzactie(self):
        try:
            id_tranzactie = input("Id-ul tranzactie: ")
            id_masina = input("Id-ul masinii: ")
            id_card = input("Id-ul cardului(0 daca nu are card): ")
            suma_piese = float(input("Suma pieselor: "))
            suma_manopera = float(input("Suma manoperei: "))
            data = input("Data(dd.mm.yyyy): ")
            ora = input("Ora(hh:mm): ")

            self.__tranzactie_service.adaugare(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_tranzactie(self):
        try:
            id_tranzactie = input("Dati Id-ul tranzactie pe care vreti sa il stergeti: ")

            self.__tranzactie_service.stergere(id_tranzactie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_tranzactie(self):
        try:
            id_tranzactie = input("Id-ul tranzactie pe care vreti sa o modificati: ")
            id_masina = input("Noul Id al masinii sau nimic daca nu vreti sa schimbati : ")
            id_card = input("Noul Id al cardului (0 daca nu are card) sau nimic daca nu vreti sa schimbati: ")
            suma_piese = float(input("Suma noua a pieselor sau 0 daca nu vreti sa schimbati: "))
            suma_manopera = float(input("Suma noua a manoperei sau 0 daca nu vreti sa schimbati: "))
            data = input("Data(dd.mm.yyyy) sau nimic daca nu vreti sa schimbati: ")
            ora = input("Ora(hh:mm) sau nimic daca nu vreti sa schimbati: ")

            self.__tranzactie_service.modificare(id_tranzactie, id_masina, id_card, suma_piese, suma_manopera, data,
                                                 ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_tranzactii(self):
        tranzactii = self.__tranzactie_service.get_all()
        for tranzactie in tranzactii:
            print(tranzactie)
