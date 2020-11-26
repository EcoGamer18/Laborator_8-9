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
                  "4.Afișarea tuturor tranzacțiilor cu suma cuprinsă într-un interval dat.\n"
                  "5.Cautare \n"
                  "6.Afisarea masinilor ordonate descrescator dupa suma obtinuta la manopera\n"
                  "7.Afișarea cardurilor client ordonate descrescător după valoarea reducerilor obținute\n"
                  "x.Iesire\n")
            option = input("Alegeti o optiune:\n")
            if option == '1':
                self.run_crud_masini()
            elif option == '2':
                self.run_crud_carduri()
            elif option == '3':
                self.run_crud_tranzactii()
            elif option == '4':
                self.ui_afisare_interval()
            elif option == '5':
                self.ui_cautare()
            elif option == '6':
                self.ui_ordonat_manopera()
            elif option == '7':
                self.ui_ordonat_reducere()
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
                  "4.Populare\n"
                  "a.Afiseaza toate cardurile\n"
                  "x.Iesire din meniul \"CRUD carduri\"\n")
            option = input("Alegeti optiunile:\n")
            if option == '1':
                self.ui_adaugare_card()
            elif option == '2':
                self.ui_stergere_card()
            elif option == '3':
                self.ui_modificare_card()
            elif option == '4':
                self.ui_populare_card()
            elif option == 'a':
                self.ui_afisare_carduri()
            elif option == 'x':
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_card(self):
        try:
            id_card = input("Id-ul cardului: ")
            nume = input("Numele clientului: ")
            prenume = input("Prenumele clientului: ")
            CNP = input("CNP-ul clientului: ")
            data_nasterii = input("Data nasterii clientului(dd.mm.yyyy): ")
            data_inregistrarii = input("Data inregistrarii(dd.mm.yyyy): ")

            self.__card_client_service.adaugare(id_card, nume, prenume, CNP, data_nasterii, data_inregistrarii)
            print(yellow("Cardul a fost adaugat.", ['italic']))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_card(self):
        try:
            id_card = input("Dati Id-ul cardului pe care vreti sa il stergeti: ")

            self.__card_client_service.stergere(id_card)
            print(yellow("Cardul a fost sters.", ['italic']))
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
            print(yellow("Cardul a fost modificat.", ['italic']))
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
            print(yellow("Tranzactia a fost adaugata.", ['italic']))
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
            print(yellow("Tranzactia a fost stearsa.", ['italic']))
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
            print(yellow("Tranzactia a fost modificata.", ['italic']))
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

    def ui_afisare_interval(self):
        try:
            inf = float(input("Introduceti capatul inf al intervalului: "))
            sup = float(input("Introduceti capatul sup al intervalului: "))
            print(f"Tranzactiile alfate in intervalul [{inf},{sup}] sunt:")
            for x in self.__tranzactie_service.tranzactii_interval(inf, sup):
                print(x)
        except Exception as e:
            print(e)

    def ui_populare_card(self):
        n = int(input("Introduceti un numar n: "))
        self.__card_client_service.populatie(n)

    def ui_cautare(self):
        while True:
            print("1.Cautare masini\n"
                  "2.Cautare clienti\n"
                  "3.Cautare full text\n"
                  "x.Iesire din meniu \"Cautare\" \n")
            option = input("Alegeti optiunea:\n")
            if option == "1":
                self.ui_cautare_masini()
            elif option == "2":
                self.ui_cautare_clienti()
            elif option == "3":
                self.ui_cautare_full()
            elif option == "x":
                break
            else:
                print("Optiune invalida\n")

    def ui_cautare_masini(self):
        while True:
            print("1.Cautare dupa model\n"
                  "2.Cautare dupa an achizitie\n"
                  "3.Cautare dupa nr. km\n"
                  "x.Iesire din meniu \"Cautare masini\" \n")
            option = input("Alegeti optiunea:\n")
            if option == "1":
                self.ui_cautare_masini_model()
            elif option == "2":
                self.ui_cautare_masini_an()
            elif option == "3":
                self.ui_cautare_masini_km()
            elif option == "x":
                break
            else:
                print("Optiune invalida")

    def ui_cautare_masini_model(self):
        caut = input("Introduceti modelul pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        masini = self.__masina_service.get_all()
        for masina in masini:
            if masina.model.lower().find(caut) > -1:
                cautare.append(masina)
        print("Masinile cu modelul cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_masini_an(self):
        caut = input("Introduceti anul achizitiei pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        masini = self.__masina_service.get_all()
        for masina in masini:
            if str(masina.an_achizitie).lower().find(caut) > -1:
                cautare.append(masina)
        print("Masinile cu anul cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_masini_km(self):
        caut = input("Introduceti numarul de km pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        masini = self.__masina_service.get_all()
        for masina in masini:
            if str(masina.nr_km).lower().find(caut) > -1:
                cautare.append(masina)
        print("Masinile cu numarul de km cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_clienti(self):
        while True:
            print("1.Cautare dupa nume\n"
                  "2.Cautare dupa prenume\n"
                  "3.Cautare dupa CNP\n"
                  "x.Iesire din meniu \"Cautare clienti\" \n")
            option = input("Alegeti optiunea:\n")
            if option == "1":
                self.ui_cautare_clienti_nume()
            elif option == "2":
                self.ui_cautare_clienti_prenume()
            elif option == "3":
                self.ui_cautare_clienti_cnp()
            elif option == "x":
                break
            else:
                print("Optiune invalida\n")

    def ui_cautare_clienti_nume(self):
        caut = input("Introduceti numele pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        clienti = self.__card_client_service.get_all()
        for client in clienti:
            if client.nume.lower().find(caut) > -1:
                cautare.append(client)
        print("Clientii cu numele cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_clienti_prenume(self):
        caut = input("Introduceti prenumele pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        clienti = self.__card_client_service.get_all()
        for client in clienti:
            if client.prenume.lower().find(caut) > -1:
                cautare.append(client)
        print("Clientii cu prenumele cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_clienti_cnp(self):
        caut = input("Introduceti CNP-ul pe care il cautati:\n")
        caut = caut.lower()
        cautare = []
        clienti = self.__card_client_service.get_all()
        for client in clienti:
            if str(client.CNP).lower().find(caut) > -1:
                cautare.append(client)
        print("Clientii cu CNP-ul cautat sunt:")
        for i in cautare:
            print(i)

    def ui_cautare_full(self):
        caut = input("Introduceti termenul pe care il cautati:\n")
        caut = caut.lower()
        cautare_m = []
        cautare_c = []
        clienti = self.__card_client_service.get_all()
        masini = self.__masina_service.get_all()
        for masina in masini:
            if masina.model.lower().find(caut) > -1 or str(masina.an_achizitie).lower().find(caut) > -1 or str(
                    masina.nr_km).lower().find(caut) > -1:
                cautare_m.append(masina)

        for client in clienti:
            if client.nume.lower().find(caut) > -1 or client.prenume.lower().find(
                    caut) > -1 or str(client.CNP).find(caut) > -1:
                cautare_c.append(client)

        print("Masinile cu termenul cautat sunt:")
        for m in cautare_m:
            print(m)

        print("Clientii cu termenul cautat sunt:")
        for c in cautare_c:
            print(c)

    def ui_ordonat_manopera(self):
        print("Masinile ordonate descrescator dupa suma obtinuta pe manopera:")
        sortat = self.__tranzactie_service.masini_dupa_manopera()
        for masina in sortat:
            print(masina[0])
            print("cu suma manoperei "+ str(masina[1]))

    def ui_ordonat_reducere(self):
        print("Cardurile ordonate descrescator dupa valoarea reducerii obtinute:")
        sortat = self.__tranzactie_service.carduri_dupa_valoarea_reducerii()
        for card in sortat:
            print(card[0])
            print("cu valoarea redusa "+str(card[1]))
