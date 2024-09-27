class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin ,destination, out_date, return_date,stops):
        self.price = price
        self.originLocationCode = origin
        self.destinationLocationCode = destination
        self.departureDate = out_date
        self.returnDate = return_date
        self.stops = stops

def cheapest_flights(data):
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A","N/A","N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    no_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    return FlightData(lowest_price,origin,destination, out_date, return_date,no_stops)