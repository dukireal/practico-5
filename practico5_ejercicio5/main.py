from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class CosntructorTorta(ABC):
    @property
    @abstractmethod
    def torta(self)->None:
        pass
    @abstractmethod
    def preparar_masa(self,indice):
        pass
    @abstractmethod
    def preparar_relleno(self,indice):
        pass
    @abstractmethod
    def agregar_decoracion(self,indice):
        pass

class ConstructorTortaConcreta(CosntructorTorta):
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self._torta=Torta()
    @property
    def torta(self)->Torta():
        torta=self._torta
        self.reset()
        return torta
    def preparar_masa(self,inidce):
        match inidce:
            case 1:
                self._torta.add("preparar masa de vainilla")
            case 2:
                self._torta.add("preparar masa de coco")
            case 3:
                self._torta.add("perparar masa de chocolate")
    def preparar_relleno(self, indice):
        match indice:
            case 1:
                self._torta.add("agregar relleno de crema chantilli")
            case 2:
                self._torta.add("agregar relleno de dulce de leche")
            case 3:
                self._torta.add("agregar relleno de durazno")
    def agregar_decoracion(self, indice):
        match indice:
            case 1:
                self._torta.add("rodear la torta con crema")
            case 2:
                self._torta.add("agregar ralladura de coco")
            case 3:
                self._torta.add("recubrir la torta con chocolate")

class Torta():
    def __init__(self) -> None:
        self.partes=[]
    def add(self,parte):
        self.partes.append(parte)

    def lista_de_partes(self):
        print(f"partes de la torta: {', '.join(self.partes)}", end="")

class Director:
    def __init__(self) -> None:
        self._builder = None
    @property
    def builder(self)->CosntructorTorta:
        return self._builder
    @builder.setter
    def builder(self,builder:CosntructorTorta)->None:
        self._builder=builder
    
    def torta_vainilla(self,indice)->None:
        self.builder.preparar_masa(indice)
        self.builder.preparar_relleno(indice)
        self.builder.agregar_decoracion(indice)
    def torta_coco(self,indice)->None:
        self.builder.preparar_masa(indice)
        self.builder.preparar_relleno(indice)
        self.builder.agregar_decoracion(indice)
    def torta_chocolate(self,indice)->None:
        self.builder.preparar_masa(indice)
        self.builder.preparar_relleno(indice)
        self.builder.agregar_decoracion(indice)

director=Director()
builder=ConstructorTortaConcreta()
director.builder=builder

print("torta de vainilla:")
director.torta_vainilla(1)
builder.torta.lista_de_partes()
print("\n")
print("torta de coco")
director.torta_coco(2)
builder.torta.lista_de_partes()
print("\n")
print("torta de chocolate")
director.torta_chocolate(3)
builder.torta.lista_de_partes()