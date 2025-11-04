class TarjetaCredito:
   pass


class Usuario:
    def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

  
    def hacer_compra(self, monto: int):  #recibe como argumento el monto de la compra
       # self.saldo_pagar = self.saldo_pagar + monto
       self.saldo_pagar += monto
       return self

    def pagar_tarjeta(self, monto: int):
       # self.saldo_pagar -= monto
       self.saldo_pagar = self.saldo_pagar - monto
       return self

    def mostrar_saldo_usuario(self):
       print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")
    
    def transferir_deuda(self, otro_usuario: "Usuario", monto: int):
       # 1. reduzca la deuda (saldo_pagar) del usuario por el monto
       self.saldo_pagar = self.saldo_pagar - monto
       # 2. agrega esa cantidad al saldo_pagar de otro_usuario
       otro_usuario.saldo_pagar = otro_usuario.saldo_pagar + monto
       

usuario_1 = Usuario(nombre="Nariyoshi",
                    apellido="Miyagi",
                    email="usuario1@mail.com")
usuario_2 = Usuario(nombre="Usuario2",
                    apellido="Apellido2",
                    email="usuario2@mail.com")
usuario_3 = Usuario(nombre="Usuario3",
                    apellido="Apellido3",
                    email="usuario3@mail.com")

# usuario_1.hacer_compra(2000)
# usuario_1.hacer_compra(3000)
# usuario_1.pagar_tarjeta(1000)

usuario_1.hacer_compra(2000).hacer_compra(3000).pagar_tarjeta(1000)

usuario_1 = usuario_1.hacer_compra(2000)
usuario_1 = usuario_1.hacer_compra(3000)
usuario_1 = usuario_1.pagar_tarjeta(1000)


usuario_1.mostrar_saldo_usuario()


usuario_2.hacer_compra(2000)
usuario_2.mostrar_saldo_usuario()

print("------------------")

usuario_1.transferir_deuda(otro_usuario=usuario_2, monto=1000)
usuario_1.mostrar_saldo_usuario()
usuario_2.mostrar_saldo_usuario()