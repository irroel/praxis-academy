class Petani():
    def __init__(self, name, lahan):
        self.lahan = lahan
        self.name = name
    def getName(self):
        return self.name
    def getLahan(self):
        return self.lahan
    # def membajak(self, lahan):
    #     self.lahan = lahan
        

class Lahan(Petani):
    def __init__(self, name, lahan):
        super().__init__(name, lahan)
           
    def membajak(self):
        return f'Pak {Petani.getName(self)}  sedang membajak  {Petani.getLahan(self)}'

l = Lahan("Praxis", "sawah")

l.membajak()
