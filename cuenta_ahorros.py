from cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, numero, nombre_propietario, saldo, interes):
        super().__init__(numero, nombre_propietario, saldo)
        self.interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
        self._interes = interes

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor < 0:
            print("No se puede tener saldos negativos en una cuenta de ahorros")
        else:
            self.saldo -= valor

    def mostrar_saldo(self):
        print("Saldo de la cuenta de ahorros:", self.saldo)

    def pagar_interes(self):
        self.saldo += self.saldo * self.interes

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta de ahorros de {self.nombre_propietario}: {self.saldo}")