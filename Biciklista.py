

class Biciklista:

    # u pythonu mozemo imati public i private atribute

    # __ovojeprivatanatribut
    # ovojepublicatribut

    # protected  

    __id : int 
    __broj_prijave : int 
    __pol : str 
    __sifra : str 
    __prva_etapa : int 
    __druga_etapa : int 


    # parametrizovani konstruktor -> konstruktor koji prihvata vrednosti za sva polja 

    def __init__(self, id, broj_prijave, pol, sifra, prva_etapa, druga_etapa) -> None:
        self.__id = id 
        self.__broj_prijave = broj_prijave
        self.__pol = pol
        self.__sifra = sifra 
        self.__prva_etapa = prva_etapa
        self.__druga_etapa = druga_etapa
    
    def __str__(self) -> str:
        return f'Id: {self.__id}\nBroj prijave: {self.__broj_prijave}\nPol: {self.__pol}\nSifra: {self.__sifra}\nPrva etapa: {self.__prva_etapa}\nDruga etapa: {self.__druga_etapa}'

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _broj_prijave(self):
        return self.__broj_prijave

    @_broj_prijave.setter
    def _broj_prijave(self, value):
        self.__broj_prijave = value

    @property
    def _pol(self):
        return self.__pol

    @_pol.setter
    def _pol(self, value):
        self.__pol = value

    @property
    def _sifra(self):
        return self.__sifra

    @_sifra.setter
    def _sifra(self, value):
        self.__sifra = value

    @property
    def _prva_etapa(self):
        return self.__prva_etapa

    @_prva_etapa.setter
    def _prva_etapa(self, value):
        self.__prva_etapa = value

    @property
    def _druga_etapa(self):
        return self.__druga_etapa

    @_druga_etapa.setter
    def _druga_etapa(self, value):
        self.__druga_etapa = value


if __name__ == "__main__":
    
    biciklista1 = Biciklista(1, 2, "muski", "test", 10, 12)
    print(biciklista1) # <__main__.Biciklista object at 0x1028beff0>
    # Id: 1
    # Broj prijave: 2
    # Pol: muski
    # Sifra: test
    # Prva etapa: 10
    # Druga etapa: 12