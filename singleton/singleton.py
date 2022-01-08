class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f"Creating the object {cls.instance}")
        return cls.instance


first_object = Singleton()
print(f"Instance ID: {id(first_object)}")

second_object = Singleton()
print(f"Instance ID: {id(second_object)}")
