class Producto():
    def __init__(self,nombre_producto,precio):
        self._nombre_producto=nombre_producto
        self._precio=precio
        
    def getprecio(self):
        pass
    def getnombre(self):
        pass

class ConcreteProducto(Producto):
    def __init__(self, nombre_producto, precio):
        super().__init__(nombre_producto, precio)
    
    def getprecio(self):
        return f"{self._precio}"
    def getnombre(self):
        return f"{self._nombre_producto}"

class Decorador(Producto):
    _componente:Producto=None
    def __init__(self,componente:Producto):
        self._componente=componente
    
    @property
    def componente(self)->Producto:
        return self._componente
    
    def getprecio(self)->str:
        return str(self._componente.getprecio())
    def getnombre(self):
        return str(self._componente.getnombre())

class MonedaArgentina(Decorador):
    def getprecio(self):
        return f"precio: AR${super().getprecio()}"
    def getnombre(self):
        return f"producto: {super().getnombre()}"

class MonedaEstadounidense(Decorador):
    def getprecio(self):
        return f"precio: U$D{super().getprecio()}"
    def getnombre(self):
        return f"preducto: {super().getnombre()}"

def cliente(producto:Producto):
    print(f"\n {producto.getnombre()},{producto.getprecio()}",end="")


algo=ConcreteProducto("jabon",90.50)
print("producto base: ")
cliente(algo)
print("\n formato argentino:")
decorador1=MonedaArgentina(algo)
cliente(decorador1)
print("\n formato estadounidense: ")
decorador2=MonedaEstadounidense(algo)
cliente(decorador2)