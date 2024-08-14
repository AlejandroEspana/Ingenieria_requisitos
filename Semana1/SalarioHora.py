class Salario:
    
    horasSemanales = int(input("ingrese las horas trabajadas: "))
    pagoHora = float(input("ingrese el pago por hora: "))

    def salarioSemanal(self):
        salario = self.horasSemanales * self.pagoHora
        print(f"su salario semanal correspondiente es de: {salario}")

empleado = Salario()
salarioSemanal = empleado.salarioSemanal()
