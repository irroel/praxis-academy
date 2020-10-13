class Petani:
    all_petani = []                     # mengakses semua instance
    def __init__(self, name, lahan):    # inisiasi
        self.name = name
        self.lahan = lahan
        Petani.all_petani.append(self)  # menambah setiap instance ke all_petani[]

class Lahan(Petani):                    # Lahan inherit from Petani
    def membajak(self, luas):
        return f'Pak {self.name}, sedang membajak {self.lahan} seluas {luas} hektar'

class Bibit(Petani):                    # Bibit inherit from Petani
    def menanam(self,bibit):
        return f'{self.lahan.title()} pak {self.name} akan ditanami {bibit}.'


print(Petani.all_petani)