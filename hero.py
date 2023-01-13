class SuperHeros():
    def __init__(self,name,superpower):
        self.name=name
        self.superpowers=superpower
    def get_superpower(self):
        print(f"I am {self.name} and my power is {self.superpowers}")
ironman=SuperHeros(
    name="Ironman",
    superpower="suit"
)
ironman.get_superpower()