class Singleton:
    __instance = None

    def __init__(self: object) -> None:
        if not Singleton.__instance:
            print("The __init__ method has been called!")
        else:
            print(f"An instance has been created: {self.get_instance()}")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


first_object = Singleton()
first_object.get_instance()

# Here one instance of Singleton has been created
second_object = Singleton()
