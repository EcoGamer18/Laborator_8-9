from Tests.test_card_service import test_adaugare_card, test_stergere_card, test_modificare_card
from Tests.test_domain import test_tranzactie, test_card, test_masina
from Tests.test_masina_service import test_adauga_masina, test_stergere_masina, test_modificare_masina


def run_all():
    test_masina()
    test_card()
    test_tranzactie()

    test_adauga_masina()
    test_stergere_masina()
    test_modificare_masina()

    test_adaugare_card()
    test_stergere_card()
    test_modificare_card()