# class NumeroMayor:

#     A = float(input("introduzca el valor del primer numero: "))
#     B = float(input("introduzca el valor del segundo numero: "))

#     def Mayor(self):
#         if self.A > self.B:
#             print("el primer numero es mayor")
#         else:
#             print("el segundo numero es mayor")

# mayor = NumeroMayor()
# mayor.Mayor()

class NumeroMayor:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def Mayor(self):
        if self.A > self.B:
            print("El primer número es mayor")
        elif self.A == self.B:
            print("los numeros son iguales")
        else:
            print("El segundo número es mayor")


A = float(input("Introduzca el valor del primer número: "))
B = float(input("Introduzca el valor del segundo número: "))

num_mayor = NumeroMayor(A, B)
num_mayor.Mayor()
