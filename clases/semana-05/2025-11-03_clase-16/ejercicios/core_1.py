"""
- Cuando se crea una nueva instancia de TarjetaCredito se da el monto, de lo contrario el saldo_pagar se establece como $0 -> saldo_pagar debe tener valor predeterminado 0
- La tarjeta debe tener también un límite de crédito, que se va a proporcionar en la creación de la instancia -> limite_credito es un atributo
- Por último, la tarjeta de crédito tendrá intereses, los cuales deben guardarse como decimales; por ejemplo: si tiene 2% de interés, se guardará 0.02 -> intereses es un atributo float
"""

class TarjetaCredito:

    # Incluye en este método valores por default

    # 
    def __init__(self, saldo_pagar, limite_credito, intereses):
        # TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)
        pass

    def compra(self, monto):
        # TU CODIGO
        pass

    def pago(self, monto):
        # TU CODIGO
        pass

    def mostrar_info_tarjeta(self):
        # TU CODIGO
        pass

    def cobrar_interes(self):
        # TU CODIGO
        pass
