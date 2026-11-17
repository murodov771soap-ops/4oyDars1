class KvadratTenglama:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminant(self):
        return self.b**2 - 4 * self.a * self.c

    def yechim(self):
        d = self.diskriminant()
        if d < 0:
            print("Haqiqiy yechim mavjud emas")
        elif d == 0:
            x = -self.b / (2 * self.a)
            print(f"Bitta yechim: x = {x}")
        else:
            x1 = (-self.b + d**0.5) / (2 * self.a)
            x2 = (-self.b - d**0.5) / (2 * self.a)
            print(f"Ikkita yechim: x1 = {x1}, x2 = {x2}")


t1 = KvadratTenglama(1, -3, 2)
t2 = KvadratTenglama(1, -2, 1)
t3 = KvadratTenglama(1, 2, 5)

t1.yechim()
t2.yechim()
t3.yechim()