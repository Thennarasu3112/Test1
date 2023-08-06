class ATM():
    def __init__(self,Bank_name=None,year=None,model=None):
        self.Bank_name = Bank_name
        self.year = year
        self.model = model

    def __str__(self):
        return (f"Object ATM generated for {self.Bank_name}.")

if __name__ == "__main__":
    atm1 = ATM('IND','2023','13')
    print(atm1)
