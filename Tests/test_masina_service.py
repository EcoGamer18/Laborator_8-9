from Domain.masina_validator import MasinaValidator
from Repository.file_repository import FileRepository
from Service.masina_service import MasinaService
from Tests.utilities import clear_file


def test_adauga_masina():
    clear_file("masini-service-test.txt")
    masini_repository = FileRepository("masini-service-test.txt")
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)

    service.adaugare('1', 'Mercedes', 1998, 450000, "NU")
    assert len(service.get_all()) == 1
    added = masini_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.model == 'Mercedes'
    assert added.an_achizitie == 1998
    assert added.nr_km == 450000
    assert added.garantie == 'NU'

    try:
        service.adaugare('1', 'Mercedes', 1998, 450000, "NU")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_stergere_masina():
    clear_file("masini-service-test.txt")
    masini_repository = FileRepository("masini-service-test.txt")
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)
    service.adaugare('1', 'Mercedes', 1998, 450000, "NU")
    service.adaugare('2', 'Audi', 2005, 12000, "DA")

    try:
        service.stergere('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 1
    deleted = masini_repository.get_by_id('1')
    assert deleted is None
    remaining = masini_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.model == 'Audi'
    assert remaining.an_achizitie == 2005
    assert remaining.nr_km == 12000
    assert remaining.garantie == 'DA'


def test_modificare_masina():
    clear_file("masini-service-test.txt")
    masini_repository = FileRepository("masini-service-test.txt")
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)
    service.adaugare('1', 'Mercedes', 1998, 450000, "NU")
    service.adaugare('2', 'Audi', 2005, 12000, "DA")

    service.modificare('1', 'VW', 0, 0, "")
    updated = masini_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == 'VW'
    assert updated.an_achizitie == 1998
    assert updated.nr_km == 450000
    assert updated.garantie == 'NU'

    updated = masini_repository.get_by_id('2')
    assert updated is not None
    assert updated.id_entitate == '2'
    assert updated.model == 'Audi'
    assert updated.an_achizitie == 2005
    assert updated.nr_km == 12000
    assert updated.garantie == 'DA'

    try:
        service.modificare('3', "", 2020, 15222, "")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_modificare_garantie():
    clear_file("masini-service-test.txt")
    masini_repository = FileRepository("masini-service-test.txt")
    masina_validator = MasinaValidator()
    service = MasinaService(masini_repository, masina_validator)
    service.adaugare('1', 'Mercedes', 1998, 450000, "DA")
    service.adaugare('2', 'Audi', 2019, 12000, "NU")

    service.modificare_garantie()
    updated = masini_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == 'Mercedes'
    assert updated.an_achizitie == 1998
    assert updated.nr_km == 450000
    assert updated.garantie == 'NU'

    updated = masini_repository.get_by_id('2')
    assert updated is not None
    assert updated.id_entitate == '2'
    assert updated.model == 'Audi'
    assert updated.an_achizitie == 2019
    assert updated.nr_km == 12000
    assert updated.garantie == 'DA'