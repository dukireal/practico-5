from __future__ import annotations
from abc import ABC,abstractmethod

class Helper:
    def __init__(self,subsystem1:Ingles,subsystem2:Mayuscula,subsystem3:Minuscula) -> None:
        self._subsystem1=subsystem1 or Ingles()
        self._subsystem2=subsystem2 or Mayuscula()
        self._subsystem3=subsystem3 or Minuscula()
        
    def operacion(self,cadena)->str:
        resultados=[]
        resultados.append("palabra en ingles:")
        resultados.append(self._subsystem1.accion(cadena))
        resultados.append("palabras en mayuscula:")
        resultados.append(self._subsystem2.accion(cadena))
        resultados.append("palabras solo en minuscula:")
        resultados.append(self._subsystem3.accion(cadena))
        return f"\n".join(resultados)
    
class Palabras(ABC):
    def __init__(self) -> None:
        self._palabra1='hola'
        self._palabra2='auto'
        self._palabra3='moto'
        self._palabra4='chau'
        self._palabra5='gato'
        self._palabra6='perro'
    @abstractmethod
    def accion(self,palabra)->str:
        pass

class Ingles(Palabras):
    def accion(self,palabra)->str:
        if palabra==self._palabra1:
            return "hello"
        elif palabra ==self._palabra2:
            return "Car"
        elif palabra ==self._palabra3:
            return "Motorcycle"
        elif palabra==self._palabra4:
            return "Good Bye"
        elif palabra==self._palabra5:
            return "Cat"
        elif palabra==self._palabra6:
            return "Dog"
        else:
            return "palabra no reconocida o mal escrita"

class Mayuscula(Palabras):
    def accion(self,palabra)->str:
        if palabra==self._palabra1:
            return "HOLA"
        elif palabra ==self._palabra2:
            return "AUTO"
        elif palabra ==self._palabra3:
            return "MOTO"
        elif palabra==self._palabra4:
            return "CHAU"
        elif palabra==self._palabra5:
            return "GATO"
        elif palabra==self._palabra6:
            return "PERRO"
        else:
            return "palabra no reconocida o mal escrita"

class Minuscula(Palabras):
    def accion(self,palabra)->str:
        if palabra==self._palabra1:
            return "hola"
        elif palabra ==self._palabra2:
            return "auto"
        elif palabra ==self._palabra3:
            return "moto"
        elif palabra==self._palabra4:
            return "chau"
        elif palabra==self._palabra5:
            return "gato"
        elif palabra==self._palabra6:
            return "perro"
        else:
            return "palabra no reconocida o mal escrita"

def client_code(facade:Helper,cadena):
    print(facade.operacion(cadena),end="")

subsistema1=Ingles()
subsistema2=Mayuscula()
subsistema3=Minuscula()
elfacade=Helper(subsistema1,subsistema2,subsistema3)
elfacade2=Helper(subsistema1,subsistema2,subsistema3)
elfacade3=Helper(subsistema1,subsistema2,subsistema3)
palabra=input("\n ingrese una palabra: ")
client_code(elfacade,palabra)
palabra=input("\n ingrese una palabra: ")
client_code(elfacade2,palabra)
palabra=input(" \n ingrese una palabra: ")
client_code(elfacade3,palabra)