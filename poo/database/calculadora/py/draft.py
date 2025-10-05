class Calculadora:
    def __init__(self,batteryMax:int):
        self.display:float = 0
        self.batteryMax:int = batteryMax
        self.battery: int = 0

    def __str__(self) :
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, amount:int) -> None:
        self.battery += amount
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    
    def sum(self, val1: float, val2: float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.display = val1 + val2
            self.battery -= 1

        
    def div(self, numerator:float, denominator:float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif denominator == 0:
                print("fail: divisao por zero")
                self.battery -= 1
        else:
            self.display = numerator / denominator
            self.battery -= 1

def main():
    calc = Calculadora(0)
    while True:
        command: str = input()
        print ("$" + command)
        tokens: list[str] = command.split(" ")
        if tokens[0] == "end":
            break
        elif tokens[0] == "init":
            maxBattery = int (tokens[1])
            calc = Calculadora(maxBattery)
        
        elif tokens[0] == "charge":
            units: int = int (tokens[1])
            calc.charge(units)

        elif tokens[0] == "sum":
            x: float = float (tokens[1])
            y: float = float (tokens[2])
            calc.sum(x,y)

        elif tokens[0] == "div":
            x: float = float (tokens[1])
            y: float = float (tokens[2])
            calc.div(x,y)

        elif tokens[0] == "show":
            print(calc)
main()
    