class Galon:
    
    litros = float(input("ingrese la cantidad de litros producidos: "))
    precio = 31

    def Galones(self):
        i = round((self.litros / 3785),3)
        print(f"usted ha poducido {i} galones")
