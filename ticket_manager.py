class TicketManager:
    _instance = None

    def __new__(cls):
        """
        Tek bir örnek oluşturarak bilet yönetimi işlemlerini gerçekleştiren TicketManager sinifini oluşturur.

        Returns:
            TicketManager: TicketManager sinifinin örneği.
        """
        if cls._instance is None:
            cls._instance = super(TicketManager, cls).__new__(cls)
            cls._instance.tickets = []
        return cls._instance

    def add_ticket(self, ticket):
        """
        Belirtilen bilet örneğini bilet listesine ekler.

        Args:
            ticket (Ticket): Eklenecek bilet örneği.
        """
        self.tickets.append(ticket)

    def get_tickets(self):
        """
        Bilet listesini döndürür.

        Returns:
            list: Bilet örneklerinin listesi.
        """
        return self.tickets

