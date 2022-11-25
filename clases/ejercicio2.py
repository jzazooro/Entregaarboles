import pandas as pd  

class arbol(object):

    def __init__(self):
        self.nombre = None
        self.numero = None
        self.tipo = None

class pokemon(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.type1 = None
        self.type2 = None
        self.total = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.sp_atk = None
        self.sp_def = None
        self.speed = None
        self.generation = None
        self.legendary = None
        
def leerdataset(iniciar):
    iniciar=pd.read_csv('pokemon.csv')
    return iniciar