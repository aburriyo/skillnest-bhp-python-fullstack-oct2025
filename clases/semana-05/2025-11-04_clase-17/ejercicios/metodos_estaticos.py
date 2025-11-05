class TarjetaCredito:
    def __init__(self, limite_credito, saldo_pagar):
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
    
    def hacer_compra(self, monto):
        # Usar método estático para validar
        if TarjetaCredito.puede_comprar(self.limite_credito, 
                                        self.saldo_pagar, 
                                        monto):
            self.saldo_pagar += monto
            print(f"Compra de ${monto} realizada")
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite")
        return self
    
    @staticmethod
    def puede_comprar(limite: int, saldo_utilizado: int, monto: int):
        """Verifica si se puede realizar la compra"""
        return (saldo_utilizado + monto) <= limite # True | False
        #  (int + int) <= int
        # 1000 <= 50: False
        #  (int) <= int
        #  bool
    
    @staticmethod
    def calcular_interes(monto, tasa):
        """Calcula el interés sobre un monto"""
        return monto * tasa

# Usar métodos estáticos
tarjeta = TarjetaCredito(20000, 5000)
tarjeta.hacer_compra(3000)  # Compra realizada

# También se pueden usar directamente
interes = TarjetaCredito.calcular_interes(1000, 0.015)
print(f"Interés: ${interes}")  # $15.0
