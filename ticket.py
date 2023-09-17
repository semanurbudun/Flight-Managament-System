class Ticket:
    def __init__(self, ticket_number, passenger, flight, seat_number):
        """
        Bilet örneğini oluşturan Ticket sinifini temsil eder.

        Args:
            ticket_number (str): Bilet numarasi.
            passenger (Passenger): Bilet sahibi yolcu.
            flight (Flight): Uçuş bilgileri.
            seat_number (str): Koltuk numarasi.
        """
        self.ticket_number = ticket_number
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number

    def display_info(self):
        """
        Bilet bilgilerini ekrana yazdirir.
        """
        print(f"Bilet Numarasi: {self.ticket_number}")
        self.passenger.display_info()
        self.flight.display_info()
        print(f"Koltuk Numarasi: {self.seat_number}")
        print("------------------------")

