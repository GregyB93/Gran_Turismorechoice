def unindent(string):
    return ''.join(map(str.lstrip, string.splitlines(2)))

class CarOption(): 
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - £{self.price}"

class Accessory(CarOption):
    pass


class Colour(CarOption):
    pass


class Car():
    def __init__(
            self,
            model: str,
            price: int,
            colour_options: list[Colour],
            accessories: list[Accessory],
            available_accessories: list[Accessory],
        ):
        self.model = model
        self.price = price
        self.colour = colour_options[0]
        self.colour_options = colour_options
        self.accessories = accessories
        self.available_accessories = available_accessories
    
    def __str__(self):
        return f"{self.model} - £{self.calculate_total()}"    

    def add_accessory(self):
        accessory_str = list(map(lambda accessory: accessory.__str__(), self.available_accessories))
        accessory_joined = "\n\n".join(accessory_str)
        accessory: str = input(
            unindent(
                f"""
                Which accessory would you like to add?

                {accessory_joined}

                Enter a number between 1 and {len(self.available_accessories)}:
                """
            )
        )

        if (1 > int(accessory) or int(accessory) > len(self.available_accessories)):
            print("Invalid accessory")
            self.menu()
            return
        
        accessory_to_add = self.available_accessories[int(accessory) - 1]
        self.accessories.append(accessory_to_add)
        self.available_accessories.remove(accessory_to_add)
        print(f"Added {accessory_to_add} to car")
        self.edit_car() 

    def remove_accessory(self):
        accessory_str = list(map(lambda accessory: accessory.__str__(), self.accessories))
        accessory_joined = "\n\n".join(accessory_str)
        accessory: str = input(
            unindent(
                f"""
                Which accessory would you like to remove?

                {accessory_joined}

                Enter a number between 1 and {len(self.accessories)}:
                """
            )
        )

        if (1 > int(accessory) or int(accessory) > len(self.available_accessories)):
            print("Invalid accessory")
            self.menu()
            return
        
        accessory_to_remove = self.accessories[int(accessory) - 1]
        self.accessories.remove(accessory_to_remove)
        self.available_accessories.append(accessory_to_remove)
        print(f"Removed {accessory_to_remove} from car")
        self.edit_car()

    def change_colour(self, colour: Colour):
        if colour in self.colour_options:
      
            self.colour = colour
        else:
            print("Colour not permitted")

    def reset_car(self):
        self.accessories = []
        self.colour = self.colour_options[0]

    def edit_colour(self):
        colour_options_str = list(map(lambda colour: colour.__str__(), self.colour_options))
        colour_options_joined = "\n\n".join(colour_options_str)
        colour = input(
            unindent(
                f"""
                Which colour would you like to change to?

                {colour_options_joined}

                Enter a number between 1 and {len(self.colour_options)}:
                """
            )
        )

        colour = self.colour_options[int(colour) - 1]
        self.change_colour(colour)
        print(f"Changed colour to {colour}")
        self.edit_car()

    def edit_accessories(self):
        menu = input(
            unindent(
                f"""
                What would you like to do?
                1. Add an accessory
                2. Remove an accessory
                3. Back
                """
            )
        )
        if (menu == "1"):
            print("adding accessory")
            self.add_accessory()
            print("Added accessory")
            return
        if (menu == "2"):
            self.remove_accessory()
            return
        
        self.edit_car()
            
    def edit_car(self):
        menu = input(
            unindent(
                f"""
                What would you like to edit?
                1. Colour
                2. Accessories
                3. Back
                """
            )
        )
        if (menu == "1"):
            self.edit_colour()
            return
        if (menu == "2"):
            self.edit_accessories()
            return
        if (menu == "3"):
            self.menu()
            return

    def calculate_total(self):
        total = self.price + self.colour.price
        for accessory in self.accessories:
            total += accessory.price
        return total

class Garage():
    def __init__(self, cars: list[Car], car_options: list[Car]):
        self.cars = cars
        # inject the menu function into all the child car options
        for car in car_options:
            car.menu = self.menu
        self.car_options = car_options

    def calculate_total(self):
        total = 0
        for car in self.cars:
            total += car.calculate_total()
        return total

    def menu(self):
        owned_cars = "\n\n".join(map(lambda car: car.__str__(), self.cars))
        menu = input(
            unindent(
                f"""
                Welcome to Movie Motors
                --------------------

                You have {len(self.cars)} cars in your garage:
                {owned_cars}

                Your total is £{self.calculate_total()}

                --------------------
                Please choose an option:
                1. Add a car
                2. Edit a car
                3. Remove a car
                4. Exit

                """
            )
        )
        if (menu == "1"):
            self.add_car()
            return
        
        if (menu == "2"):
            if (len(self.cars) == 0):
                print("You have no cars to edit")
                self.menu()
                return
            
            self.edit_car()
            return
        if (menu == "3"):
            if (len(self.cars) == 0):
                print("You have no cars to edit")
                self.menu()
                return
            self.remove_car()
            return
       
        exit()
    
    def add_car(self):
        car_options_str = list(map(lambda car: car.__str__(), self.car_options))
        car_options_joined = "\n\n".join(car_options_str)
        car = input(
            unindent(
                f"""
                Which car would you like to add?

                {car_options_joined}

                Enter a number between 1 and {len(self.car_options)}:
                """
            )
        )

        if  int(car) < 1 or int(car) > len(self.car_options):
            print("Invalid input")
            self.menu()
            return

        car = self.car_options[int(car) - 1]
        self.cars.append(car)
        self.car_options.remove(car)
        print(f"Added {car} to garage")
        self.menu()
    
    def edit_car(self):
        car_str = list(map(lambda car: car.__str__(), self.cars))
        car_joined = "\n\n".join(car_str)
        car = input(
            unindent(
                f"""
                Which car would you like to edit?

                {car_joined}

                Enter a number between 1 and {len(self.cars)}:
                """
            )
        )

        if  int(car) < 1 or int(car) > len(self.cars):
            print("Invalid input")
            self.menu()
            return
        
        car = self.cars[int(car) - 1]
        car.edit_car()

    def remove_car(self):
        car_str = list(map(lambda car: car.__str__(), self.cars))
        car_joined = "\n\n".join(car_str)
        car = input(
            unindent(
                f"""
                Which car would you like to remove?

                {car_joined}

                Enter a number between 1 and {len(self.cars)}:
                """
            )
        )

        if  int(car) < 1 or int(car) > len(self.cars):
            print("Invalid input")
            self.menu()
            return
        
        car = self.cars[int(car) - 1]
        self.cars.remove(car)
        self.car_options.append(car.reset_car())
        print(f"Removed {car} from garage")
        self.menu()
        

def main():
    Delorean = Car("1985 DMC Delorean", 35000, [
        Colour("Standard Silver", 0),
        Colour("Futuristic Fuchsia", 50),
        Colour("Tire Flame Red", 100)
    ], [], [
        Accessory("Flux Capacitor", 1210),
        Accessory("Mr Fusion", 50),
        Accessory("Flight Capabilities", 9999)
    ])

    Aston = Car("1963 Aston Martin DB5", 7000000, [
        Colour("Shaken not stirred Silver", 0),
        Colour("Money Penny Purple", 99),
        Colour("Brown... James Brown", 199)
    ], [], [
        Accessory("Passenger Ejector Seat", 1999),
        Accessory("Machine Gun Headlights", 499),
        Accessory("Bulletproof Chassis", 9999)
    ])

    Sentinel = Car("1959 Cadillac Miller-Meteor Sentinel", 15000, [
        Colour("Classic White and Red", 0),
        Colour("Ectoplasm Green", 5),
        Colour("Crossed Stream Orange", 250)
    ], [], [
        Accessory("Siren/loudspeaker Combo", 99),
        Accessory("Ghostly Goo Deep Clean", 75),
        Accessory("Proton Pack Storage", 250)
    ])
    
    
    garage = Garage([], [Delorean, Aston, Sentinel])
    garage.menu()

if __name__ == "__main__":
    main()
