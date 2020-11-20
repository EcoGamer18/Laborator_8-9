from Domain.masina import Masina
from Domain.masina_validator import MasinaValidator
from Repository.file_repository import FileRepository


class MasinaService:
    def __init__(self, masini_repository: FileRepository, masini_validator: MasinaValidator):
        self.__masini_repository = masini_repository
        self.__masini_validator = masini_validator

    def get_all(self):
        return self.__masini_repository.get_all()

    def adaugare(self, id_masina, model, an_achizitie, nr_km, garantie):
        """:
        Adaugarea unei masini la dictionarul care reprezinta repository-ul
        """
        masina = Masina(id_masina, model, an_achizitie, nr_km, garantie)
        self.__masini_validator.validator(masina)
        self.__masini_repository.adaugare(masina)

    def stergere(self, id_masina):
        """
        Stergerea unei masini din dictionarul care reprezinta repository-ul
        """
        self.__masini_repository.stergere(id_masina)

    def modificare(self, id_masina, model, an_achizitie, nr_km, garantie):
        masina = self.__masini_repository.get_by_id(id_masina)

        if masina is None:  # daca nu exista masina cu id-ul dat
            raise KeyError(f"Nu exista deja o masina cu id-ul {id_masina}")

        if model != "":
            masina.model = model
        if an_achizitie != 0:
            masina.an_achizitie = an_achizitie
        if nr_km != 0:
            masina.nr_km = nr_km
        if garantie != "":
            masina.garantie = garantie

        self.__masini_validator.validator(masina)
        self.__masini_repository.modificare(masina)
