from Domain.card_client import CardClient
from Domain.masina import Masina
from Domain.tranzactie import Tranzactie


def test_masina():
    masina=Masina('1','Audi',2004,25645,"DA")
    assert masina.id_entitate == '1'
    assert masina.model == 'Audi'
    assert masina.an_achizitie == 2004
    assert masina.nr_km == 25645
    assert masina.garantie == "DA"

def test_card():
    card=CardClient('1','Popescu','Dan','6001015334568','01.10.2000','15.10.2010')
    assert card.id_entitate == '1'
    assert card.nume == 'Popescu'
    assert card.prenume == 'Dan'
    assert card.CNP == '6001015334568'
    assert card.data_nasterii == '01.10.2000'
    assert card.data_inregistrarii == '15.10.2010'

def test_tranzactie():
    tranzactie=Tranzactie('1','1','1',156,205,'18.02.2019','15:56',True,False,15,15)
    assert tranzactie.id_entitate == '1'
    assert tranzactie.id_masina == '1'
    assert tranzactie.id_card_client == '1'
    assert tranzactie.suma_piese == 156
    assert tranzactie.suma_manopera == 205
    assert tranzactie.data == '18.02.2019'
    assert tranzactie.ora == '15:56'
    assert tranzactie.reducere_card == True
    assert tranzactie.reducere_garantie == False
    assert tranzactie.s_p_redusa == 15
    assert tranzactie.s_m_redusa == 15

