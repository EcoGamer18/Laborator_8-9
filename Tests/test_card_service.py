from Domain.card_client_validator import CardValidator
from Repository.file_repository import FileRepository
from Service.card_client_service import CardClientService
from Tests.utilities import clear_file


def test_adaugare_card():
    clear_file("card-service-test.txt")
    card_repository = FileRepository("card-service-test.txt")
    card_validator = CardValidator()
    service = CardClientService(card_repository, card_validator)

    service.adaugare('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003')
    assert len(service.get_all()) == 1
    added = card_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'Popescu'
    assert added.prenume == 'Dan'
    assert added.CNP == '5000121223541'
    assert added.data_nasterii == "18.01.2001"
    assert added.data_inregistrarii == '04.11.2003'

    try:
        service.adaugare('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_stergere_card():
    clear_file("card-service-test.txt")
    card_repository = FileRepository("card-service-test.txt")
    card_validator = CardValidator()
    service = CardClientService(card_repository, card_validator)

    service.adaugare('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003')
    service.adaugare('2', 'Pop', 'Teodor', '5004522364123', "17.12.2005", '05.04.2007')

    try:
        service.stergere('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 1
    deleted = card_repository.get_by_id('1')
    assert deleted is None
    remaining = card_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.nume == 'Pop'
    assert remaining.prenume == 'Teodor'
    assert remaining.CNP == '5004522364123'
    assert remaining.data_nasterii == "17.12.2005"
    assert remaining.data_inregistrarii == '05.04.2007'


def test_modificare_card():
    clear_file("card-service-test.txt")
    card_repository = FileRepository("card-service-test.txt")
    card_validator = CardValidator()
    service = CardClientService(card_repository, card_validator)

    service.adaugare('1', 'Popescu', 'Dan', '5000121223541', "18.01.2001", '04.11.2003')
    service.adaugare('2', 'Pop', 'Teodor', '5004522364123', "17.12.2005", '05.04.2007')

    service.modificare('1', '', '', '5012348567982', '', '18.09.2019')
    updated = card_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume == 'Popescu'
    assert updated.prenume == 'Dan'
    assert updated.CNP == '5012348567982'
    assert updated.data_nasterii == "18.01.2001"
    assert updated.data_inregistrarii == '18.09.2019'

    remaining = card_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.nume == 'Pop'
    assert remaining.prenume == 'Teodor'
    assert remaining.CNP == '5004522364123'
    assert remaining.data_nasterii == "17.12.2005"
    assert remaining.data_inregistrarii == '05.04.2007'

    try:
        service.modificare('3', "", '', '1524356112485', '', '')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
