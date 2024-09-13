from database import db

class Imoveis(db.Model):
    
    __tablename__= "Imoveis"
    id_imoveis = db.Column(db.Integer, primary_key = True)
    endereco = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    valor = db.Column(db.Float(10,2))

    def __init__(self, endereco, tipo, valor):
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return "<Endereço {}>".format(self.endereco)