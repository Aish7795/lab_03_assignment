class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_by_city(self, city):
        return [flight for flight in self.flights if flight.source == city or flight.destination == city]

    def get_flights_from_city(self, city):
        return [flight for flight in self.flights if flight.source == city]

    def get_flights_between_cities(self, source, destination):
        return [flight for flight in self.flights if flight.source == source and flight.destination == destination]

def main():
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    flight_table = FlightTable()

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    print("Select search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter city code: ")
        city_flights = flight_table.get_flights_by_city(city)
        if city_flights:
            print("Flights for {}: ".format(city))
            for flight in city_flights:
                print(flight.flight_id, flight.source, flight.destination, flight.price)
        else:
            print("No flights found for {}.".format(city))
    elif choice == 2:
        city = input("Enter city code: ")
        from_city_flights = flight_table.get_flights_from_city(city)
        if from_city_flights:
            print("Flights from {}: ".format(city))
            for flight in from_city_flights:
                print(flight.flight_id, flight.source, flight.destination, flight.price)
        else:
            print("No flights found from {}.".format(city))
    elif choice == 3:
        source = input("Enter source city code: ")
        destination = input("Enter destination city code: ")
        between_cities_flights = flight_table.get_flights_between_cities(source, destination)
        if between_cities_flights:
            print("Flights between {} and {}: ".format(source, destination))
            for flight in between_cities_flights:
                print(flight.flight_id, flight.source, flight.destination, flight.price)
        else:
            print("No flights found between {} and {}.".format(source, destination))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()