from Domain.card_client_validator import CardValidator
from Domain.masina_validator import MasinaValidator
from Domain.tranzactie_validator import TranzactieValidator
from Repository.file_repository import FileRepository
from Service.card_client_service import CardClientService
from Service.masina_service import MasinaService
from Service.tranzactie_service import TranzactieService
from Tests.run_all_tests import run_all
from UI.console import Consola


def main():
    masini_repository = FileRepository('masini.txt')
    masina_validator = MasinaValidator()
    carduri_repository = FileRepository('carduri.txt')
    carduri_validator = CardValidator()
    tranzactii_repository = FileRepository('tranzactii.txt')
    tranzactii_validator = TranzactieValidator()
    masina_service = MasinaService(masini_repository, masina_validator)

    carduri_service = CardClientService(carduri_repository, carduri_validator)
    tranzactii_service = TranzactieService(tranzactii_repository, masini_repository, carduri_repository,tranzactii_validator)

    console = Consola(masina_service, carduri_service, tranzactii_service)
    console.run_menu()


run_all()
main()
