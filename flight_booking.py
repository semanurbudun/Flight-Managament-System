class FlightBooking:
    def __init__(self, ticket, airline, booking_time):
        """
        Uçuş Rezervasyonu sinifi, bir bilet, bir hava yolu ve rezervasyon zamani ile bir uçuş rezervasyonunu temsil eder.

        Args:
            ticket (Ticket): Uçuş biletini temsil eden bir nesne.
            airline (Airline): Hava yolunu temsil eden bir nesne.
            booking_time (str): Rezervasyonun yapildiği zaman bilgisi.
        """
        self.ticket = ticket
        self.airline = airline
        self.booking_time = booking_time

    def display_info(self):
        """
        Uçuş Rezervasyonu bilgilerini ekrana yazar.
        """
        print("Uçuş Rezervasyonu Detaylari:")
        print(f"Rezervasyon Zamani: {self.booking_time}")
        self.ticket.display_info()
        self.airline.display_info()


