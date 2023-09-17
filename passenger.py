class Passenger:
    def __init__(self, name, passport_number):
        """
        Yolcu bilgilerini temsil eden bir Yolcu sinifi oluşturur.

        Args:
            name (str): Yolcu adi.
            passport_number (str): Pasaport numarasi.
        """
        self.name = name
        self.passport_number = passport_number

    def display_info(self):
        """
        Yolcu bilgilerini ekrana yazdirir.
        """
        print("Yolcu Bilgileri:")
        print(f"Ad: {self.name}")
        print(f"Pasaport Numarasi: {self.passport_number}")
        print("------------------------")

