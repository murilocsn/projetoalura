from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_praca = Restaurante('praça','gourmet')

restaurante_praca.alternar_status()

prato_lasanha = Prato('lasanha', 25.00, 'deliciosa lasanha de carne')
bebida_coca = Bebida('coca-cola', 8.00, 'lata')



def main():
    print(restaurante_praca)
    print(prato_lasanha)
    print(bebida_coca)

if __name__ == "__main__":
    main()
