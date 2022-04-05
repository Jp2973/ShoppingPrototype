class Address:
    def __init__(self):
        self.addressLineOne: str = None
        self.addressLineTwo: str = None
        self.city: str = None
        self.state: str = None
        self.zip: int = None

    def __str__(self):
        return f'{self.addressLineOne}\n{self.addressLineTwo}\n{self.city}, {self.state} {self.zip}'
