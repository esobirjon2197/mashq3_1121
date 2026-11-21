class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def malumot(self):
        print(f"Kitob: {self.nomi}")
        print(f"Muallif: {self.muallif}")

    def sotib_olish(self):
        print("Kitob sotib olindi.")


class ElektronKitob(Kitob):
    def __init__(self, nomi, muallif, format):
        super().__init__(nomi, muallif)
        self.format = format

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}")

    def sotib_olish(self):
        super().sotib_olish()
        print("Elektron nusxa yuklab olishga tayyor.")


kitob = ElektronKitob(
    "Python asoslari",
    "Anvar Narzullayev",
    "PDF"
)

kitob.malumot()
kitob.sotib_olish()
