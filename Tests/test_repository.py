from Domain.masina import Masina
from Repository.file_repository import FileRepository
from Tests.utilities import clear_file


def test_adaugare_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")

    masina1 = Masina('1', "Audi", 2002, 156000, "DA")

    entitati_repository.adaugare(masina1)
    assert len(entitati_repository.get_all()) == 1
    added = entitati_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.model == 'Audi'
    assert added.an_achizitie == 2002
    assert added.nr_km == 156000
    assert added.garantie == "DA"

    try:
        masina2 = Masina('1', "Mercedes", 1998, 15230, "NU")
        entitati_repository.adaugare(masina2)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_stergere_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")

    masina1 = Masina('1', "Audi", 2002, 156000, "DA")
    masina2 = Masina('2', "Mercedes", 1998, 15230, "NU")

    entitati_repository.adaugare(masina1)
    entitati_repository.adaugare(masina2)

    try:
        entitati_repository.stergere('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    entitati_repository.stergere('1')
    assert len(entitati_repository.get_all()) == 1
    deleted = entitati_repository.get_by_id('1')
    assert deleted is None
    remaining = entitati_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.model == "Mercedes"
    assert remaining.an_achizitie == 1998
    assert remaining.nr_km == 15230
    assert remaining.garantie == "NU"


def test_modificare_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")

    masina1 = Masina('1', "Audi", 2002, 156000, "DA")
    masina2 = Masina('2', "Mercedes", 1998, 15230, "NU")

    entitati_repository.adaugare(masina1)
    entitati_repository.adaugare(masina2)

    masina3 = Masina('1', "VW", 1996, 156000, "DA")
    entitati_repository.modificare(masina3)
    updated = entitati_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == "VW"
    assert updated.an_achizitie == 1996
    assert updated.nr_km == 156000
    assert updated.garantie == "DA"

    unchanged = entitati_repository.get_by_id('2')
    assert unchanged is not None
    assert unchanged.id_entitate == '2'
    assert unchanged.model == "Mercedes"
    assert unchanged.an_achizitie == 1998
    assert unchanged.nr_km == 15230
    assert unchanged.garantie == "NU"

    try:
        masina4 = Masina('3', '', 1996, 15682, '')
        entitati_repository.modificare(masina4)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
