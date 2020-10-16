from ibmcloudant.cloudant_v1 import CloudantV1
from math import pow
from math import sqrt


class AirportService:

    def __init__(self):
        self.airport_service = CloudantV1.new_instance(service_name="AIRPORTS")
        self.airport_service.set_service_url('https://mikerhodes.cloudant.com')
        self.db_name = "airportdb"
        self.user_input = self.collect_user_input()
        self.query_data = self.collect_query_data()

    def search_airports(self):
        print('Searching for airports by the following parameters: lon:[' +
              self.query_data["from_lat"] + ' TO ' + self.query_data["to_lat"] + '] AND lat:[' +
              self.query_data["from_lon"] + ' TO ' + self.query_data["to_lon"] + ']')

        airport_search_response = self.airport_service.post_search(
            db=self.db_name,
            ddoc='view1',
            index='geo',
            query='lon:[' + self.query_data["from_lat"] + ' TO ' + self.query_data["to_lat"] + '] AND lat:[' +
                  self.query_data["from_lon"] + ' TO ' + self.query_data["to_lon"] + ']'
        ).get_result()

        return self.find_and_sort_airports(airport_search_response)

    def find_and_sort_airports(self, airport_search_response):
        airports = []
        if "rows" in airport_search_response:
            for airport in airport_search_response["rows"]:
                current_distance = self.calculate_distance_between_two_points(airport["fields"]["lat"],
                                                                              airport["fields"]["lon"])
                if current_distance <= self.user_input["rad"]:
                    airport["distance"] = current_distance
                    airports.append(airport)
        return sorted(airports, key=lambda k: k['distance'])

    def printEnd(self, airports):
        if (airports != []):
            for airport in airports:
                try:
                    print("Name: " + airport["fields"]["name"] + ", Distance: " + str(airport["distance"]))
                except:
                    print("An exception occurred")
        else:
            print("Couldn't find airports with the given parameters, exiting the program...")

    def calculate_distance_between_two_points(self, lat, lon):
        return sqrt(pow(abs(self.user_input["lat"] - lat), 2) + pow(abs(self.user_input["lon"] - lon), 2))

    def collect_user_input(self):
        return {
            "lat": self.get_valid_input("Latitude: ", "lat"),
            "lon": self.get_valid_input("Longitude: ", "lon"),
            "rad": self.get_valid_input("Radius: ", "rad"),
        }

    def collect_query_data(self):
        return {
            "from_lat": str(self.user_input["lat"] - self.user_input["rad"]),
            "to_lat": str(self.user_input["lat"] + self.user_input["rad"]),
            "from_lon": str(self.user_input["lon"] - self.user_input["rad"]),
            "to_lon": str(self.user_input["lon"] + self.user_input["rad"])
        }

    def get_valid_input(self, prompt, type):
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Please provide a number.")
                continue
            if (type == "lat") and ((value < -90) or (value > 90)):
                print("Please provide a valid latitude (between -90 and 90).")
                continue
            elif (type == "lon") and ((value < -180) or (value > 180)):
                print("Please provide a valid longitude (between -180 and 180).")
                continue
            elif (type == "rad") and (value < 0):
                print("Please provide a positive number for radius.")
                continue
            else:
                break

        return value


def main():
    print("Welcome to the airport searcher! Please enter the following parameters:")
    airport_service = AirportService()
    airport_service.printEnd(airport_service.search_airports())


if __name__ == "__main__":
    main()
