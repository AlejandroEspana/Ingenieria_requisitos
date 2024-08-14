class Galon:
    
    litros = float(input("ingrese la cantidad de litros producidos: "))
    precio = float(input("ingrese el precio por galon: "))

    def Galones(self):
        i = round((self.litros / 3785),3)
        return i

    def pago(self):
        b = round(self.Galones()*self.precio)
        print(f"el precio de los galones producidos es de: {b}")

empresa = Galon()
pago = empresa.pago()