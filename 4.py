class Doira:
    def init(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2

    def uzunlik(self):
        return 2 * 3.14 * self.radius


d1 = Doira(3)
d2 = Doira(5)
d3 = Doira(10)

for d in (d1, d2, d3):
    print(f"Radius: {d.radius}, Yuza: {d.yuza()}, Uzunlik: {d.uzunlik()}")