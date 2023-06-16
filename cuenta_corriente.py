from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero, nombre_propietario, saldo, tiene_chequera):
        super().__init__(numero, nombre_propietario, saldo)
        self.tiene_chequera = tiene_chequera

    @property
    def tiene_chequera(self):
        return self._tiene_chequera

    @tiene_chequera.setter
    def tiene_chequera(self, tiene_chequera):
        self._tiene_chequera = tiene_chequera

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor < 0:
            print("No se puede tener saldos negativos en una cuenta corriente")
        else:
            self.saldo -= valor

    def mostrar_saldo(self):
        print("Saldo de la cuenta corriente:", self.saldo)

    def pagar_cheque(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta corriente de {self.nombre_propietario}: {self.saldo}")