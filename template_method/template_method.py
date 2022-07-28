from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    @abstractmethod
    def going(self):
        pass

    @abstractmethod
    def day_one(self):
        pass

    @abstractmethod
    def day_two(self):
        pass

    @abstractmethod
    def day_three(self):
        pass

    @abstractmethod
    def trip_return(self):
        pass

    def itinerary(self):
        self.going()
        self.day_one()
        self.day_two()
        self.day_three()
        self.trip_return()


class TripToVinice(Trip):
    def going(self):
        print("airplane trip")

    def day_one(self):
        print("visit the basilica of san marquis")

    def day_two(self):
        print("visit to doge palace")

    def day_three(self):
        print("enjoy the food near the Rialto bridge")

    def trip_return(self):
        print("return by plane")


class TripToFortaleza(Trip):
    def going(self):
        print("bus trip")

    def day_one(self):
        print("visit the Iracema beach")

    def day_two(self):
        print("visit to Beach Park Resort")

    def day_three(self):
        print("visit to Villa Gale Resort")

    def trip_return(self):
        print("return by bus")


class AgencyTrip:
    def choice_trip(self):
        choice: str = input("Which place do you like to travel [F]Fortaleza/[V]Venice: ")

        if choice.lower() == "f":
            self.trip = TripToFortaleza()
            self.trip.itinerary()
        elif choice.lower() == "v":
            self.trip = TripToVinice()
            self.trip.itinerary()
        else:
            print("Sorry, we do not have this trip option yet! =(")


if __name__ == "__main__":
    agency = AgencyTrip()
    agency.choice_trip()
