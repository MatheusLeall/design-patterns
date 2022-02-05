class EventManagement:
    def __init__(self) -> None:
        print("EventManagement :: I will organize with everyone!\n\n")

    def organize(self):
        self.party_room = PartyRoom()
        self.party_room.schedule_appointment()

        self.florist = Florist()
        self.florist.flower_arrangement()

        self.food = Restaurant()
        self.food.cook()

        self.music = Band()
        self.music.set_up_stage()


# Subsystem 1
class PartyRoom:
    def __init__(self) -> None:
        print("PartyRoom :: Scheduling party room for the matrimony")

    def _is_available(self):
        print("PartyRoom :: Is this party room available?")
        return True

    def schedule_appointment(self):
        if self._is_available():
            print("PartyRoom :: Scheduled\n")


# Subsystem 2
class Florist:
    def __init__(self) -> None:
        print("Florist :: Flowers for the event")

    def flower_arrangement(self):
        print("Florist :: Roses, daisies and lilies will be used\n")


# Subsystem 3
class Restaurant:
    def __init__(self) -> None:
        print("Restaurant :: Food for the event")

    def cook(self):
        print("Restaurant :: Chinese and Brazilian Food\n")


# Subsystem 4
class Band:
    def __init__(self) -> None:
        print("Band :: Music for the event")

    def set_up_stage(self):
        print("Band :: Preparing stage to play jazz and rock in the event\n")


# Client
class Client:
    def __init__(self) -> None:
        print("client :: I'm getting married!")

    def hire_event_manager(self):
        print("Client :: I'll hire an event manager\n")

        event_management = EventManagement()
        event_management.organize()

    def __del__(self):
        print("Client :: it was very simple to organize the matrimony!\n")


if __name__ == "__main__":
    client = Client()
    client.hire_event_manager()
