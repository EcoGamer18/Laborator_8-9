from Domain.card_client import CardClient
from Domain.masina import Masina
from Domain.tranzactie_validator import TranzactieValidator
from Repository.file_repository import FileRepository
from Service.tranzactie_service import TranzactieService
from Tests.utilities import clear_file


def test_adaugare_tranzactie():
    clear_file('tranzactii-test.txt')
    tranzactii_repository = FileRepository("tranzactii-test.txt")
    clear_file("masini-test.txt")
    masini_repository = FileRepository('masini-test.txt')
    clear_file("carduri-test.txt")
    carduri_repository = FileRepository('carduri-test.txt')
    tranzactii_validator= TranzactieValidator()
    service = TranzactieService(tranzactii_repository, masini_repository, carduri_repository,tranzactii_validator)
    carduri_repository.adaugare(CardClient('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003'))
    masini_repository.adaugare(Masina('1', 'Mercedes', 1998, 450000, "NU"))
    service.adaugare('1', '1', '1', 152, 1562, '18.10.2012', '15:10')
    assert len(service.get_all()) == 1
    added = tranzactii_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.id_masina == '1'
    assert added.id_card_client == '1'
    assert added.suma_piese == 152
    assert added.suma_manopera == 1562
    assert added.data == '18.10.2012'
    assert added.ora == '15:10'

    try:
        service.adaugare('1', '2', '3', 152, 1562, '18.10.2012', '15:10')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    try:
        service.adaugare('2', '1', '8', 152, 1562, '18.10.2012', '15:10')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    try:
        service.adaugare('2', '4', '1', 152, 1562, '18.10.2012', '15:10')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_stergere_tranzactie():
    clear_file('tranzactii-test.txt')
    tranzactii_repository = FileRepository("tranzactii-test.txt")
    clear_file("masini-test.txt")
    masini_repository = FileRepository('masini-test.txt')
    clear_file("carduri-test.txt")
    carduri_repository = FileRepository('carduri-test.txt')
    tranzactii_validator = TranzactieValidator()
    service = TranzactieService(tranzactii_repository, masini_repository, carduri_repository, tranzactii_validator)
    carduri_repository.adaugare(CardClient('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003'))
    masini_repository.adaugare(Masina('1', 'Mercedes', 1998, 450000, "NU"))
    service.adaugare('1', '1', '1', 152, 1562, '18.10.2012', '15:10')

    try:
        service.stergere('2')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 0


def test_modificare_tranzactie():
    clear_file('tranzactii-test.txt')
    tranzactii_repository = FileRepository("tranzactii-test.txt")
    clear_file("masini-test.txt")
    masini_repository = FileRepository('masini-test.txt')
    clear_file("carduri-test.txt")
    carduri_repository = FileRepository('carduri-test.txt')
    tranzactii_validator = TranzactieValidator()
    service = TranzactieService(tranzactii_repository, masini_repository, carduri_repository, tranzactii_validator)
    carduri_repository.adaugare(CardClient('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003'))
    masini_repository.adaugare(Masina('1', 'Mercedes', 1998, 450000, "NU"))
    service.adaugare('1', '1', '1', 152, 1562, '18.10.2012', '15:10')

    service.modificare('1', '', '', 1526, 48888, '', '')
    updated = tranzactii_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.id_masina == '1'
    assert updated.id_card_client == '1'
    assert updated.suma_piese == 1526
    assert updated.suma_manopera == 48888
    assert updated.data == '18.10.2012'
    assert updated.ora == '15:10'
