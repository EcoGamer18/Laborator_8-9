from Repository.file_repository import FileRepository
from Service.tranzactie_service import TranzactieService
from Tests.utilities import clear_file


def test_adaugare_tranzactie():
    clear_file('tranzactii-test.txt')
    tranzactii_repository=FileRepository("tranzactii-test.txt")
    clear_file("masini-test.txt")
    masini_repository=FileRepository('masini-test.txt')
    clear_file("carduri-test.txt")
    carduri_repository=FileRepository('carduri-test.txt')
    service=TranzactieService(tranzactii_repository,masini_repository,carduri_repository)
    carduri_repository.adaugare()
