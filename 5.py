class Talaba:
    def init(self, ism, yosh, ball):
        self.ism = ism
        self.yosh = yosh
        self.ball = ball

    def natija(self):
        if self.ball >= 86:
            return "A"
        elif self.ball >= 71:
            return "B"
        elif self.ball >= 56:
            return "C"
        else:
            return "F"


s1 = Talaba("Ali", 19, 92)
s2 = Talaba("Vali", 20, 78)
s3 = Talaba("Soli", 18, 45)

for s in (s1, s2, s3):
    print(f"{s.ism}, {s.yosh} yosh, {s.ball} ball -> {s.natija()}")