from Tests.test_domain import test_tranzactie, test_card, test_masina
from Tests.test_masina_service import test_adauga_masina, test_stergere_masina, test_modificare_masina


def run_all():
    test_masina()
    test_card()
    test_tranzactie()

    test_adauga_masina()
    test_stergere_masina()
    test_modificare_masina()