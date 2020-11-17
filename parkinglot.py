
class CarParking():
    def __init__(self, no_of_parking=6):
        self.no_of_parking = no_of_parking
        self.current_slot = 1
        self.car_count = 0
        self.leave_car_slot_no = []
        self.parking_data = dict()
        for i in range(no_of_parking):
            self.parking_data[i+1] = "empty"
        print(f"Created a parking lot with {no_of_parking} slots")

    def park_car(self, car_no, car_colour):
        if self.car_count < self.no_of_parking or len(self.leave_car_slot_no) != 0:  # noqa
            if self.parking_data[self.current_slot] != "empty":
                self.current_slot = self.leave_car_slot_no[0]
                self.leave_car_slot_no.pop(0)

            self.parking_data[self.current_slot] = [car_no, car_colour]
            self.current_slot += 1
            self.car_count += 1
            return f'Allocated slot number : {self.current_slot-1}'

        else:
            return "Sorry, Parking is Full Wait for some time"

    def leave_car(self, slot_no):
        if slot_no > 0 and slot_no <= self.no_of_parking:
            self.parking_data[slot_no] = "empty"
            self.leave_car_slot_no.append(slot_no)
            self.car_count -= 1
            self.current_slot -= 1
            # self.current_slot = slot_no

            return f'Slot number {slot_no} is free'
        else:
            return "Hey, Please enter correct slot no."

    def get_reg_no_by_colour(self, color_name):
        all_car = []
        for i in self.parking_data.values():
            if i == "empty":
                continue
            else:
                car_no, color = i
                if color == color_name:
                    all_car.append(car_no)

        return "No car with this colour" if len(all_car) == 0 else ", ".join(all_car)  # noqa

    def get_slot_no_by_colour(self, color_name):
        all_slot_no = []
        for key in self.parking_data:
            i = self.parking_data[key]
            if i == "empty":
                continue
            else:
                if i[1] == color_name:
                    all_slot_no.append(str(key))

        return "No car with this colour" if len(all_slot_no) == 0 else ", ".join(all_slot_no)  # noqa

    def get_slot_no_by_reg(self, reg_no):
        all_slot_no = []
        for key in self.parking_data:
            i = self.parking_data[key]
            if i == "empty":
                continue
            else:

                if i[0] == reg_no:
                    all_slot_no.append(str(key))

        return "No car with this Registration No." if len(all_slot_no) == 0 else ", ".join(all_slot_no)  # noqa

    def status(self):
        print("Slot No. Registratio No. Colour")
        for key in self.parking_data:
            i = self.parking_data[key]
            if i == "empty":
                continue
            else:
                print(f"{key} {i[0]} {i[1]}")


print("---------- Welcome ----------")
print("Choose one option :-")
print("1. You want to get the result through file :-")
print("2. You want to do it manually :-")

choice = int(input("Enter you choice:-"))
if choice == 1:
    parking_lot = None
    with open('command.txt', 'r') as commands:
        for command in commands:
            command = list(command.split())
            if "exit" in command and len(command) == 1:
                print("Closing the parking lot system")
                break
            elif "create_parking_lot" in command and len(command) == 2:
                parking_lot = CarParking(int(command[1]))
            elif "park" in command and len(command) == 3:
                print(parking_lot.park_car(command[1], command[2]))
            elif "leave" in command and len(command) == 2:
                print(parking_lot.leave_car(int(command[1])))
            elif "registration_numbers_for_cars_with_colour" in command and len(command) == 2:  # noqa
                print(parking_lot.get_reg_no_by_colour(str(command[1])))
            elif "slot_numbers_for_cars_with_colour" in command and len(command) == 2:  # noqa
                print(parking_lot.get_slot_no_by_colour(command[1]))
            elif "slot_number_for_registration_number" in command and len(command) == 2:  # noqa
                print(parking_lot.get_slot_no_by_reg(command[1]))
            elif "status" in command and len(command) == 1:
                parking_lot.status()
            else:
                print("Please enter correct command")
elif choice == 2:
    print("You have to follow these command to navigate the project:-")
    print("1. To create parking lot use 'create_parking_lot no.(by default is 6)'")  # noqa
    print("2. To park car in parking lot use 'park car_no. car_color'")
    print("3. To leave car in parking lot use 'leave slot_no'")
    print("4. To get status of parking lot use 'status'")
    print("5. To get registration for car with color of parking lot use ' registration_numbers_for_cars_with_colour color_name '")  # noqa
    print("6. To get slot for car with color of parking lot use ' slot_numbers_for_cars_with_colour color_name '")  # noqa
    print("7. To get slot for car with registration of parking lot use ' slot_number_for_registration_number car_no.'")  # noqa
    print()
    print("To exit type 'exit'")
    print()

    print("Enter your command")
    parking_lot = None
    while True:
        print()
        command = list(input("").split())
        if "exit" in command and len(command) == 1:
            print("Closing the parking lot system")
            break
        elif "create_parking_lot" in command and len(command) == 2:
            parking_lot = CarParking(int(command[1]))
        elif "park" in command and len(command) == 3:
            print(parking_lot.park_car(command[1], command[2]))
        elif "leave" in command and len(command) == 2:
            print(parking_lot.leave_car(int(command[1])))
        elif "registration_numbers_for_cars_with_colour" in command and len(command) == 2:  # noqa
            print(parking_lot.get_reg_no_by_colour(str(command[1])))
        elif "slot_numbers_for_cars_with_colour" in command and len(command) == 2:  # noqa
            print(parking_lot.get_slot_no_by_colour(command[1]))
        elif "slot_number_for_registration_number" in command and len(command) == 2:  # noqa
            print(parking_lot.get_slot_no_by_reg(command[1]))
        elif "status" in command and len(command) == 1:
            parking_lot.status()
        else:
            print("Please enter correct command")


else:
    print("You Choice is in correct please restart your program")


# create = CarParking(6)
# print(create.park_car("KA-01-HH-1234", "White"))
# print(create.park_car("KA-01-HH-9999", "White"))
# print(create.park_car("KA-01-BB-0001", "Black"))
# print(create.park_car("KA-01-HH-7777", "Red"))
# print(create.park_car("KA-01-HH-3141", "Blue"))
# print(create.park_car("KA-01-HH-3141", "Black"))
# print(create.leave_car(4))
# print(create.leave_car(1))
# print(create.leave_car(2))
# print(create.leave_car(3))
# create.status()
# print(create.park_car("KA-01-P-333 ", "White"))
# print(create.park_car("DL-12-AA-9999 ", "White"))
# print(create.get_reg_no_by_colour("White"))
# print(create.get_slot_no_by_colour("White"))
# print(create.get_slot_no_by_reg("KA-01-HH-3141"))
# print(create.get_slot_no_by_reg("MH-04-AY-1111"))
