# OLVERA HERRERA SHIRLEY BRIGGITT
from abc import ABC, abstractmethod
class Cuenta(ABC):
    def __init__(self, numero, nombre_propietario, saldo):
        self.numero = numero
        self.nombre_propietario = nombre_propietario
        self.saldo = saldo
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero
    @property
    def nombre_propietario(self):
        return self._nombre_propietario
    @nombre_propietario.setter
    def nombre_propietario(self, nombre_propietario):
        self._nombre_propietario = nombre_propietario
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    @abstractmethod
    def credito(self, valor):
        pass
    @abstractmethod
    def debito(self, valor):
        pass
    @abstractmethod
    def mostrar_saldo(self):
        pass