class FlightSchedule:
    _instance = None

    def __new__(cls):
        """
        Uçuş Programi sinifinin bir örneğini oluşturur veya mevcut örneği döndürür.
        Bu yöntem, sinifin örneğinin yalnizca bir kez oluşturulmasini sağlar.

        Returns:
            FlightSchedule: Uçuş Programi sinifinin bir örneği.
        """
        if cls._instance is None:
            cls._instance = super(FlightSchedule, cls).__new__(cls)
            cls._instance.flights = []
        return cls._instance

    def add_flight(self, flight):
        """
        Uçuşlari programina ekler.

        Args:
            flight (FlightBooking): Eklenmek istenen uçuş rezervasyonu.
        """
        self.flights.append(flight)

    def get_flights(self):
        """
        Programdaki tüm uçuş rezervasyonlarini döndürür.
        Returns:
            list: Uçuş rezervasyonlarinin listesi.
        """
        return self.flights
    
    
