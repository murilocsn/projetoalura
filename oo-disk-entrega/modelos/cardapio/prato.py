from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    _pratos = []
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao.title()
        Prato._pratos.append(self)


    def __str__(self):
        return self._nome