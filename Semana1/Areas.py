class AreaFigura:

    a = float(input("ingrese el valor de A: "))
    b = float(input("ingrese el valor de B: "))
    c = float(input("ingrese el valor de C: "))

    def AreaRectangulo(self):
        resultado = self.b*self.c
        return resultado

    def AreaTriangulo(self):
        resultado = ((self.a-self.c)*self.b)/2
        return resultado

    def AreaTotal(self):
        print(self.AreaRectangulo()+self.AreaTriangulo())
