class Picina: 

    altura = float(input("introduzca la altura de la picina: "))
    ancho = float(input("introduzca el ancho de la picina: "))
    largo = float(input("introduzca el largo de la picina: "))
    pagoMetroCubico = int(input("introduzca el precio por metro cubico: "))

    def Volumen(self):
        return (self.ancho * self.altura * self.largo)
    
    def Costo(self):
        pago = self.pagoMetroCubico * self.Volumen()
        print(f"el costo total sera de {pago}")

duenio = Picina()
duenio.Costo()