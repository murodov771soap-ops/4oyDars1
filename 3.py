class Mashina:
    def init(self, nomi, rangi, yili):
        self.nomi = nomi
        self.rangi = rangi
        self.yili = yili

    def malumot(self):
        print(f"Nomi: {self.nomi}, Rangi: {self.rangi}, Yili: {self.yili}")


m1 = Mashina("Chevrolet Gentra", "Oq", 2020)
m2 = Mashina("Chevrolet Malibu", "Qora", 2022)
m3 = Mashina("Kia K5", "Kulrang", 2023)

m1.malumot()
m2.malumot()
m3.malumot()