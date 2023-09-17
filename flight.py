class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        """
        Uçuş bilgilerini temsil eden bir Uçuş sinifi oluşturur.

        Args:
            flight_number (str): Uçuş numarasi.
            origin (str): Kalkiş noktasi.
            destination (str): Variş noktasi.
            departure_time (str): Kalkiş saati.
            arrival_time (str): Variş saati.
        """
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_info(self):
        """
        Uçuş bilgilerini ekrana yazdirir.
        """
        print("Uçuş Bilgileri:")
        print(f"Uçuş Numarasi: {self.flight_number}")
        print(f"Kalkiş Noktasi: {self.origin}")
        print(f"Variş Noktasi: {self.destination}")
        print(f"Kalkiş Saati: {self.departure_time}")
        print(f"Variş Saati: {self.arrival_time}")
        print("------------------------")

