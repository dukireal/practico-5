from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

# -> anotation, permite indicar que es lo que se devuelve, pero no obliga.
    @abstractmethod
    def factory_method(self):
        pass

    def get_precio(self) -> str:
        product = self.factory_method()
        result = f"precio total:{product.calcular_precio()}"

        return result


class ConcreteCreator1(Creator):
    def __init__(self,id_juego,precio,agg) -> None:
            self._id_juego=id_juego
            self._precio=precio
            self._agg=agg
    def factory_method(self) -> Product:
        return ConcreteProductJuegoFisico(self._id_juego,self._precio,self._agg)

class ConcreteCreator2(Creator):
        def __init__(self,id_juego,precio,agg) -> None:
            self._id_juego=id_juego
            self._precio=precio
            self._agg=agg
        
        def factory_method(self) -> Product:
            return ConcreteProductJuegoDigital(self._id_juego,self._precio,self._agg)


class Product(ABC):
    def __init__(self,id_juego,precio) -> None:
        self._id_juego=id_juego
        self._precio=precio
    @abstractmethod
    def calcular_precio(self) -> str:
        pass

class ConcreteProductJuegoFisico(Product):
    def __init__(self, id_juego, precio,delivery) -> None:
        super().__init__(id_juego, precio)
        self._delivery=delivery
        
    def calcular_precio(self) -> str:
        self._precio+=self._delivery
        return self._precio


class ConcreteProductJuegoDigital(Product):
    def __init__(self, id_juego, precio,comision) -> None:
        super().__init__(id_juego, precio)
        self._comicion=comision
        
    def calcular_precio(self) -> str:
        self._precio=self._precio+(self._precio*self._comicion)
        return self._precio


def client_code(creator: Creator) :
        print(creator.get_precio())


print("precio juego fisico")
client_code(ConcreteCreator1(1,1200,200))
print("\n")

print("precio juego digital")
client_code(ConcreteCreator2(1,1200,0.25))