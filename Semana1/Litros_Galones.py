class Galon:
    
    litros = float(input("ingrese la cantidad de litros producidos: "))

    def Galones(self):
        i = round((self.litros / 3785),3)
        print(f"usted ha poducido {i} galones")
