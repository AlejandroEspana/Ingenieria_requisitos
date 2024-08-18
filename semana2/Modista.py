class modista:
    
    metrosRequeridas = float(input("ingrese el valor de Metros de tela requeridos: "))
    
    def metrosPulgadas(self):
        i = round(self.metrosRequeridas / 0.0254)
        print(f"las pulgadas que desea comprar son: {i} pulgadas")
    
seniora = modista()
seniora.metrosPulgadas()
        