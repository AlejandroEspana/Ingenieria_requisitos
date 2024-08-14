class Galon:
    
    litros = float(input("ingrese la cantidad de litros producidos: "))
    precio = float(input("ingrese el precio por galon: "))

    def Galones(self):
        i = round((self.litros / 3785),3)
        return i

    def pago(self):
        i = self.Galones()*self.precio
        print("el precio de los galones producidos es de: {i})
