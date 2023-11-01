from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    def __init__(self,nombre) -> None:
        self._nombre=nombre

    @property
    def parent(self, name) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Archivo(Component):
        
    def operation(self)->str:
        return self._nombre

class Carpeta(Component):

    def __init__(self,nombre) -> None:
        self._children: List[Component] = []
        self._nombre=nombre

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"{self._nombre} :({'+'.join(results)})"

def cliente(component:Carpeta):
    print(f"result:{component.operation()}",end="")

carpeta1=Carpeta("MLS")
carpeta1.add(Archivo("messi"))
carpeta1.add(Archivo("sergio busquets"))
carpeta1.add(Archivo("dani alves"))
nombre=Archivo("soteldo")

carpeta2=Carpeta("LPF")
carpeta2.add(Archivo("colo barco"))
carpeta2.add(Archivo("la bestia merentiel"))

arbol=Carpeta("general")
arbol.add(carpeta1)
arbol.add(carpeta2)
arbol.add(nombre)
cliente(arbol)
