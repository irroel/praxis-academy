class Petani():
    def __init__(self, name):
        # self.lahan = lahan
        self.name = name
    # def membajak(self, lahan):
    #     self.lahan = lahan
        

class Lahan(Petani):
    def __init__(self, name, lahan):
        super.__init__(self, name, lahan)
    def membajak(self, lahan):
        self.lahan = lahan
        return f'Pak {name}, membajak {lahan}.'

p = Petani("Praxis")

print(p.name)


l = Lahan("Prax", "sawah")
print(l.name)
print(l.lahan)
l.membajak("sawah")