class Airline:
    def __init__(self, name, code):
        """
        Havayolu sinifi, adi ve kodu ile bir havayolunu temsil eder.

        Args:
            name (str): Havayolunun adi.
            code (str): Havayolunun kodu.
        """
        self.name = name
        self.code = code

    def display_info(self):
        """
        Havayolu bilgilerini ekrana yazar.
        """
        print(f"Havayolu Adi: {self.name}")
        print(f"Havayolu Kodu: {self.code}")
        print("------------------------")

