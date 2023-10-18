from __future__ import annotations
from abc import ABC, abstractmethod


class Creador (ABC):
    @abstractmethod
    def factory_method():
        pass
    
    def comprar(self):
        carrito=self.factory_method()
        resultado=f"nose {carrito.getPrecio()}"
        return resultado


class CreadorJuegosDigitales(Creador):
    def factory_method(self) -> Juegos:
        return CreadorJuegosDigitales()

class CreadorJuegosFisicos(Creador):
    def factory_method(self) -> Juegos:
        return CreadorJuegosFisicos()


class Juegos(ABC):
    def __init__(self,id_juego,precio):
        self._id_juego=id_juego
        self._precio=precio
    
    def calcularimporte(self,recargo,precio):
        precio+=precio*recargo
        return precio
    
    @abstractmethod
    def getPrecio(self) -> float:
        pass

class JuegoDigital(Juegos):
    def __init__(self, id_juego, precio,empresa):
        super().__init__(id_juego, precio)
        self._empresa=empresa
        
    def getPrecio(self) -> float:
        match self._empresa:
            case 1:
                return self.calcularimporte(0.15,self._precio) 
            case 2:
                return self.calcularimporte(0.20,self._precio) 
            case 3:
                return self.calcularimporte(0.25,self._precio) 


class JuegoFisico(Juegos):
    def __init__(self, id_juego, precio,delivery):
        super().__init__(id_juego, precio)
        self._delivery=delivery
        
    def getPrecio(self) -> float:
        match self._delivery:
            case 1:
                return self.calcularimporte(0.30,self._precio) 
            case 2:
                return self.calcularimporte(0.0,self._precio) 


def comprar_juego(creator: Creador):
    print("usuario generico compra juego generico...")
    print(f"{creator.comprar()}",end="")


print("comprar por juego fisico")
id_juego=int(input("id del juego:"))
precio=float(input("ingrese precio del juego"))
delivery=int(input("inngrese el tipo de retiro: \n_1-delivery(+ %30) \n2-retiro en sucursal(sin coste adicional)"))
comprar_juego(CreadorJuegosFisicos())
print("comprar juego digital:")
empresa_juego=int(input("ingrse la plataforma difital para comprar el juego: \n1: steam (+%15)\n2:origin(+%20)\n3:epicgames(+%30)"))
comprar_juego(CreadorJuegosDigitales())