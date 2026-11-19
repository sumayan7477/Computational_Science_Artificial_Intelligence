import numpy as np

def analyze_routes(routes):
    departures =set()
    destinations =set()

    for departure , destination in routes:
        departures.add(departure)
        destinations.add(destination)

    airports = departures | destinations

    departure_only = departures - destinations
    destination_only = destinations - departures

    return departures, destinations , airports , departure_only , destination_only

def airport_array(airports):
    airport_list = list(airports)
    airport_list.sort()

    return np.array(airport_list)

def airport_statistics(routes, airports):
    route_count = len(routes)
    airport_count= len(airports)

    return route_count , airport_count



def print_report(routes, departures, destinations, airports, departure_only, destination_only, airport_array):
    print("AIRPORT REPORT")
    print(f"\nRoutes: {len(routes)}")
    print(f"\nDeparture-only airports:")
    print(departure_only)
    print(f"\nAirport array:")
    print(airport_array)
    route_count, airport_count = airport_statistics(routes, airports)
    print(f"\nStatistics")
    print(f"Routes: {route_count}")
    print(f"Airports: {airport_count}")

def main():

    routes = [
        ("HEL", "LHR"), ("HEL", "CDG"), ("LHR", "JFK"), ("CDG", "AMS"), ("AMS", "HEL"), 
        ("MAD", "BCN"), ("JFK", "LAX"), ("LAX", "HND"), ("HND", "SYD"), ("HEL", "AMS"),
    ]

    (departures, destinations, airports, departure_only, destination_only) = analyze_routes(routes)

    airport_arr = airport_array(airports)

    print_report(routes, departures, destinations, airports, departure_only, destination_only, airport_arr)
main()
