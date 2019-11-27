#la aplicaion web usa modgodb y sql  pero intranet Oracle y orientBD hambas tienen diferentes implementaciones


from abc import ABC, abstractmethod

class Lamborghini(ABC):
     @abstractmethod
     def rapido(self):
         pass
     @abstractmethod
     def lujoso(self):
        pass

class AventadorSVJ(Lamborghini):
    def rapido(self):
        return MongoDB()

    def lujoso(self):
        return SQLServerDB()


class Huracan(Lamborghini):
    def rapido(self):
        return OrientDB()

    def lujoso(self):
        return OracleDB()


class Toyota(ABC):
    @abstractmethod
    def hybrid(self):
        pass

class Fiat(ABC):
    @abstractmethod
    def economico(self):
        pass
    @abstractmethod
    def austero(self):
        pass


class FiatUno(Fiat):
    def economico(self):
        print("Fiat Uno called;")
    def austero(self):
        print("Fiat Uno called;")

class FiatMobi(Fiat):
    def economico(self):
        print("Fiat Mobit called;")
    def austero(self):
        print("Fiat Mobi called;")


class Prius(Toyota):
    def hybrid(self):
        print("Prius called;")
    

class CamryHybrid(Toyota):
    def hybrid(self):
        print("Camry Hybrid called;")
   

class Client:
    def get_database(self):
        abs_factory=AventadorSVJ()
        sql_factory=abs_factory.rapido()
        sql_factory.hybrid()
        #NoSQL------------------
        sql_factory=abs_factory.lujoso()
        sql_factory.economico()
        sql_factory.austero()
        #IntranetFactory
        abs_factory=Huracan()
        sql_factory=abs_factory.rapido()
        sql_factory.hybrid()
        #Nosql
        sql_factory=abs_factory.lujoso()
        sql_factory.economico()
        sql_factory.austero()

c=Client()
c.get_database()
        
     
