# VILLACIS BOHORQUEZ MICHAEL ROBERT
from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente
cuenta_ahorros = CuentaAhorros(numero=1, nombre_propietario="Dario Gomez", saldo=2000, interes=0.05)
cuenta_ahorros.mostrar_saldo()
cuenta_ahorros.pagar_interes()
cuenta_ahorros.mostrar_saldo()
print('\n')
print("******************\n")
cuenta_corriente = CuentaCorriente(numero=2, nombre_propietario="Liseth Pin", saldo=3000, tiene_chequera=True)
cuenta_corriente.mostrar_saldo()
cuenta_corriente.pagar_cheque(700)
cuenta_corriente.mostrar_saldo()