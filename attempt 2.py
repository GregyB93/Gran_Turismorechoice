class Car:
    def __init__(self, model, colour, accessories, price):
        self.model = model
        self.colour = colour
        self.accessories = accessories
        self.price = price

    def details(self):
        print(
            "Model: " + self.model + "\nColour: " + self.colour + "\nAccessories: " + ", ".join(self.accessories) +
            "\nPrice: £" + str(self.price))


class Colour:
    def __init__(self, name, colour_price):
        self.name = name
        self.colour_price = colour_price


class Accessory:
    def __init__(self, name, accessory_price):
        self.name = name
        self.accessory_price = accessory_price


# Base Car Models
Delorean = Car("1985 DMC Delorean", "Standard Silver", [], 35000)
Aston = Car("1963 Aston Martin DB5", "Shaken not Stirred Silver", [], 7000000)
Cadillac = Car("1959 Cadillac Miller-Meteor Sentinel", "Ghostly White", [], 15000)

# Colours
StandardSilver = Colour("Standard Silver", 0)
FuturisticFuchsia = Colour("Futuristic Fuschia", 50)
TireFlameRed = Colour("Tire Flame Red", 100)
ShakenNotStirredSilver = Colour("Shaken not Stirred Silver", 0)
MoneyPennyPurple = Colour ("Money Penny Purple", 99)
BrownJamesBrown = ("Brown... James Brown", 199)
ClassicWhiteandRed = Colour("Classic White and Red", 0)
EctoplasmGreen = Colour("Ectoplasm Green", 5)
CrossedStreamOrange = Colour("Crossed Stream Orange", 250)

while True:
    print('''
Welcome to Movie Motors
--------------------
Please select your model:
1. 1985 DMC Delorean
2. 1963 Aston Martin DB5
3. 1959 Cadillac Miller-Meteor Sentinel
''')

    model_selection = input("Enter a number 1 - 3: ")
    while True:
        if model_selection == "1":
            while True:
                print()
                Delorean.details()
                print()
                print("Would you like to change colour? ")
                change_colour = input("Enter Y/N: ")
                if change_colour.capitalize() == "Y":
                    print('''
Available colours:
1. Standard Silver + £0  
2. Futuristic Fuchsia +£50
3. Tire Flame Red +£100
''')
                    delorean_colour = input("Enter a selection 1 - 3: ")
                    if delorean_colour == "1":
                        Delorean.colour = "Standard Silver"
                        break
                    elif delorean_colour == "2":
                        Delorean.colour = "Futuristic Fuchsia"
                        Delorean.price += 50
                        break
                    elif delorean_colour == "3":
                        Delorean.colour = "Tyre Flame Red"
                        Delorean.price += 100
                        break
                    else:
                        print("Invalid selection. Please enter 1, 2, or 3.")
                        delorean_colour = input("Enter a selection 1 - 3: ")
                else:
                    break
            print()
            print("Colour updated to: " + Delorean.colour)
            Delorean.details()
            accessories_added = []
            while True:
                print()
                print("Would you like to add any accessories?")
                print('''
Available accessories:
1. Flux Capacitor +£1210
2. Mr Fusion +£50
3. Flight Capabilities +£9999
4. Done
''')
                delorean_accessories = input("Enter a selection 1 - 4: ")
                if delorean_accessories == "1" and "Flux Capacitor" not in accessories_added:
                    Delorean.accessories.append("Flux Capacitor")
                    Delorean.price += 1210
                    accessories_added.append("Flux Capacitor")
                    print("You've added: Flux Capacitor")
                elif delorean_accessories == "2" and "Mr Fusion" not in accessories_added:
                    Delorean.accessories.append("Mr Fusion")
                    Delorean.price += 50
                    accessories_added.append("Mr Fusion")
                    print("You've added: Mr Fusion")
                elif delorean_accessories == "3" and "Flight Capabilities" not in accessories_added:
                    Delorean.accessories.append("Flight Capabilities")
                    Delorean.price += 9999
                    accessories_added.append("Flight Capabilities")
                    print("You've added: Flight Capabilities")
                elif delorean_accessories == "4":
                    print("Done adding accessories.")
                    break
                else:
                    print()
                    print("You already have that! Please enter 1, 2, 3, or 4.")

            print()
            print("Here's your car: ")
            Delorean.details()
            print("Would you like to choose another model?")
            choose_another_model = input("Enter Y/N: ")
            if choose_another_model.capitalize() == "N":
                print("Enjoy your new car!")
                exit()
            elif choose_another_model.capitalize == "Y":
                break
        break

    while True:
        if model_selection == "2":
            while True:
                print()
                Aston.details()
                print()
                print("Would you like to change colour? ")
                change_colour = input("Enter Y/N: ")
                if change_colour.capitalize() == "Y":
                    print('''
Available colours:
1. Shaken not stirred Silver + £0  
2. Money Penny Purple +£99
3. Brown... James Brown +£199
''')
                    aston_colour = input("Enter a selection 1 - 3: ")
                    if aston_colour == "1":
                        Aston.colour = "Shaken not stirred Silver"
                        break
                    elif aston_colour == "2":
                        Aston.colour = "Money Penny Purple"
                        Aston.price += 99
                        break
                    elif aston_colour == "3":
                        Aston.colour = "Brown... James Brown"
                        Aston.price += 199
                        break
                    else:
                        print("Invalid selection. Please enter 1, 2, or 3.")
                        aston_colour = input("Enter a selection 1 - 3: ")
                else:
                    break
            print()
            print("Colour updated to: " + Aston.colour)
            Aston.details()
            accessories_added = []
            while True:
                print()
                print("Would you like to add any accessories?")
                print('''
Available accessories:
1. Passenger Ejector Seat +£1999
2. Machine Gun Headlights +£499
3. Bulletproof Chassis +£9999
4. Done
''')
                aston_accessories = input("Enter a selection 1 - 4: ")
                if aston_accessories == "1" and "Passenger Ejector Seat" not in accessories_added:
                    Aston.accessories.append("Passenger Ejector Seat")
                    Aston.price += 1999
                    accessories_added.append("Passenger Ejector Seat")
                    print("You've added: Passenger Ejector Seat")
                elif aston_accessories == "2" and "Machine Gun Headlights" not in accessories_added:
                    Aston.accessories.append("Machine Gun Headlights")
                    Aston.price += 499
                    accessories_added.append("Machine Gun Headlights")
                    print("You've added: Machine Gun Headlights")
                elif aston_accessories == "3" and "Bulletproof Chassis" not in accessories_added:
                    Aston.accessories.append("Bulletproof Chassis")
                    Aston.price += 9999
                    accessories_added.append("Bulletproof Chassis")
                    print("You've added: Bulletproof Chassis")
                elif aston_accessories == "4":
                    print("Done adding accessories.")
                    break
                else:
                    print()
                    print("You already have that! Please enter 1, 2, 3, or 4.")

            print()
            print("Here's your car: ")
            Aston.details()
            print("Would you like to choose another model?")
            choose_another_model = input("Enter Y/N: ")
            if choose_another_model.capitalize() == "N":
                print("Enjoy your new car!")
                exit()
            elif choose_another_model.capitalize == "Y":
                break
        break

    while True:
        if model_selection == "3":
            while True:
                print()
                Cadillac.details()
                print()
                print("Would you like to change colour? ")
                change_colour = input("Enter Y/N: ")
                if change_colour.capitalize() == "Y":
                    print('''
Available colours:
1. Classic White and Red + £0  
2. Ectoplasm Green +£5
3. Crossed Stream Orange +£250
''')
                    cadillac_colour = input("Enter a selection 1 - 3: ")
                    if cadillac_colour == "1":
                        Cadillac.colour = "Classic White and Red"
                        break
                    elif cadillac_colour == "2":
                        Cadillac.colour = "Ectoplasm Green"
                        Cadillac.price += 5
                        break
                    elif cadillac_colour == "3":
                        Cadillac.colour = "Crossed Stream Orange"
                        Cadillac.price += 250
                        break
                    else:
                        print("Invalid selection. Please enter 1, 2, or 3.")
                        cadillac_colour = input("Enter a selection 1 - 3: ")
                else:
                    break
            print()
            print("Colour updated to: " + Cadillac.colour)
            Cadillac.details()
            accessories_added = []
            while True:
                print()
                print("Would you like to add any accessories?")
                print('''
Available accessories:
1. Siren/loudspeaker Combo +99
2. Ghostly Goo Deep Clean +75
3. Proton Pack Storage +250
4. Done
''')
                cadillac_accessories = input("Enter a selection 1 - 4: ")
                if cadillac_accessories == "1" and "Siren/loudspeaker Combo" not in accessories_added:
                    Cadillac.accessories.append("Siren/loudspeaker Combo")
                    Cadillac.price += 99
                    accessories_added.append("Siren/loudspeaker Combo")
                    print("You've added: Siren/loudspeaker Combo")
                elif cadillac_accessories == "2" and "Ghostly Goo Deep Clean" not in accessories_added:
                    Cadillac.accessories.append("Ghostly Goo Deep Clean")
                    Cadillac.price += 75
                    accessories_added.append("Ghostly Goo Deep Clean")
                    print("You've added: Ghostly Goo Deep Clean")
                elif cadillac_accessories == "3" and "Proton Pack Storage" not in accessories_added:
                    Cadillac.accessories.append("Proton Pack Storage")
                    Cadillac.price += 250
                    accessories_added.append("Proton Pack Storage")
                    print("You've added: Proton Pack Storage")
                elif cadillac_accessories == "4":
                    print("Done adding accessories.")
                    break
                else:
                    print()
                    print("You already have that! Please enter 1, 2, 3, or 4.")

            print()
            print("Here's your car: ")
            Cadillac.details()
            print("Would you like to choose another model?")
            choose_another_model = input("Enter Y/N: ")
            if choose_another_model.capitalize() == "N":
                print("Enjoy your new car!")
                exit()
            elif choose_another_model.capitalize == "Y":
                break
        break
