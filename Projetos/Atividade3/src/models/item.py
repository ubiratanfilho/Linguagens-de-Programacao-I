import uuid

class Item():
    # Construtor
    def __init__(self, preco, nome, descricao=None,imagem=None):
        self._id = uuid.uuid4()
        self._preco = preco # _ indica que é privado
        self._nome = nome
        self._descricao = descricao
        self._imagem = imagem
    
    # Getters
    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_preco(self):
        return self._preco
    def get_descricao(self):
        return self._descricao
    def get_imagem(self):
        return self._imagem
    
    # To String
    def __str__(self):
        return f"{self._id} - {self._nome} - {self._preco} - {self._descricao}"
    
    def __eq__(self, __o: object):
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False
    
item = Item(20.99, "Ubiratec Start", "Primeiro Produto Ubiratec", "https")
print(item)