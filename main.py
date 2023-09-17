from flight import Flight
from passenger import Passenger
from ticket import Ticket
from airline import Airline
from airport import Airport
from flight_schedule import FlightSchedule
from ticket_manager import TicketManager
from flight_booking import FlightBooking

if __name__ == "__main__":
    # Sınıfları burada kullanabilirsiniz ve uygun nesneleri oluşturabilirsiniz.
    # ...

    # Örneğin:
    flight1 = Flight("TK123", "IST", "LAX", "2023-07-20 10:00", "2023-07-20 18:00")
    flight2 = Flight("EK456", "LAX", "DXB", "2023-07-21 12:00", "2023-07-22 03:00")

    passenger1 = Passenger("John Doe", "ABC123456")
    passenger2 = Passenger("Jane Smith", "XYZ789012")

    ticket1 = Ticket("T123456", passenger1, flight1, "A23")
    ticket2 = Ticket("T987654", passenger2, flight2, "B15")

    # FlightSchedule ve TicketManager kullanımı
    flight_schedule = FlightSchedule()
    flight_schedule.add_flight(flight1)
    flight_schedule.add_flight(flight2)

    ticket_manager = TicketManager()
    ticket_manager.add_ticket(ticket1)
    ticket_manager.add_ticket(ticket2)


    # FlightBooking kullanımı
    flight_booking1 = FlightBooking(ticket1, Airline("Turkish ", "TK"), "2023-07-19 15:00")
    flight_booking2 = FlightBooking(ticket2, Airline("Emirates", "EK"), "2023-07-20 09:30")

    # Bilgileri ekrana yazdıralım
    print("Flight Schedule:")
    for flight in flight_schedule.get_flights():
        flight.display_info()

    print("\nTicket Manager:")
    for ticket in ticket_manager.get_tickets():
        ticket.display_info()

    print("\nFlight Bookings:")
    flight_booking1.display_info()
    flight_booking2.display_info()

