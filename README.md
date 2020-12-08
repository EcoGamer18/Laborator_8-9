# Laborator_8-9
Fiecare student primește o problemă de mai jos. Trebuie predat:
  1. Săptămâna 1: 
    
    a. Mate-info:  toate  CRUD-urile,  minim  încă  o  funcționalitate  diferită  de  CRUD. 
      Cu validări,  arhitectură  stratificată  cu  toate  elementele  descrise  la  curs. 
      Salvarea datelor în fișiere.
    
    b. Mate:   toate   CRUD-urile,   cu   validări,   eventual   fără   repository.   
      Salvarea datelor în memorie.
  2. Săptămâna 2:
    
    a. Mate-info:   toate   funcționalitățile.   
      Repository   generic,   clase   proprii   de excepții. 
      Folosirea câmpurilor private.
    
    b. Mate:  toate  funcționalitățile,  eventual  fără  repository.  Salvarea datelorîn memorie.
    
***C. Service auto***

1. CRUD mașină: id, model, an achiziție, nr. km, în garanție. Km și anul fabricației să fie strict pozitivi.
2. CRUD card client: id, nume, prenume, CNP, data nașterii (dd.mm.yyyy), data înregistrării (dd.mm.yyyy). CNP-ul trebuie să fie unic.
3. CRUD tranzacție:  id, id_mașină, id_card_client (poate fi nul), sumă piese, sumă manoperă, data și ora. Dacă există un card client, atunci aplicați o reducere de 10% pentru manoperă. Dacă mașina este în garanție, atunci piesele sunt gratis. Se tipărește prețul plătit și reducerile acordate.
4. Căutare mașini și clienți după model, an fabricație, prenume, CNP etc. Căutare full text.
5. Afișarea tuturor tranzacțiilor cu suma cuprinsă într-un interval dat.
6. Afișarea mașinilor  ordonate descrescător după suma obținută pe manoperă.
7. Afișarea cardurilor client ordonate descrescător după valoarea reducerilor obținute.
8. Ștergerea tuturor tranzacțiilor dintr-un anumit interval de zile.
9. Actualizarea garanției la fiecare mașină: o mașină este în garanție dacă și numai dacă are maxim 3 ani și maxim 60.000 de km.

L8. Popularea unui repository la un anumit obiect

L9. Export Excel.

**Atentie! Foloseste jsonpickle, xlxswritter si random**

Random|Excel
-------|--------
[Links random -1](https://stackoverflow.com/questions/40921767/generate-list-of-random-names-python)|[Links Excel -1](https://www.datacamp.com/community/tutorials/python-excel-tutorial)
[Links random -2](https://pynative.com/python-get-random-float-numbers/)|[Links Excel -2](https://www.geeksforgeeks.org/reading-excel-file-using-python/)
[Links random -3](https://docs.python.org/3/library/random.html)|[Links Excel -3](https://realpython.com/openpyxl-excel-spreadsheets-python/)
[Links random -4](https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/)|[Links Excel -4](https://xlsxwriter.readthedocs.io/)
<br>|[Links Excel -5](https://stackabuse.com/reading-and-writing-excel-files-in-python-with-the-pandas-library/)

