class Airport:
    def __init__(self, name, code, location):
        """
        Havalimani sinifi, adi, kodu ve konumu ile bir havalimanini temsil eder.

        Args:
            name (str): Havalimaninin adi.
            code (str): Havalimaninin kodu.
            location (str): Havalimaninin konumu.
        """
        self.name = name
        self.code = code
        self.location = location

    def display_info(self):
        """
        Havalimani bilgilerini ekrana yazar.
        """
        print(f"Havalimani Adi: {self.name}")
        print(f"Havalimani Kodu: {self.code}")
        print(f"Konum: {self.location}")
        print("------------------------")

