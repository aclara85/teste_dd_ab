class Towel: 
    def __init__(self, color:str, size: str): #construtor
        self.color="red"
        self.size="p"
        self.wetness="0"

        def __str__(self):
            return f"color:"

towel = Towel("green", "G")
toalha = Towel("red", "G")
outra = Towel("green", "G")
toalha = Towel("red", "G")
print(towel.color)
towel.color="white"
print(towel.color)
print(towel.size)
print(towel.wetness)