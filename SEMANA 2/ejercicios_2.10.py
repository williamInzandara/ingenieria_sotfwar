class MetrosAPulgadas:
    def __init__(self, metros):
        self.metros = metros
    
    def convertir(self):
        return self.metros * 39.3701

metros = int(input("Da la medida de la tela en metros: "))
conversion = MetrosAPulgadas(metros)
pulgadas = conversion.convertir()
print(f"{metros} metros son {pulgadas} pulgadas.")