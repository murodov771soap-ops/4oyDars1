class Telefon:
    def __int__(self,model: str,rang,narx, yil=2026):
        self.module = model
        self. rang =rang
        self.narx =narx
        self.yil = yil
        print("Yangi telefon tayyor")
        
    
    def malumot(self):
        print(self.module,self.narx,self.rang,self.yil)
        
        
t1 = Telefon(model="iphone 14",rang="oq",narx=600)
t2 = Telefon("Samsung S20","Qora"250,2024)

t1.malumot()
t2.malumot()