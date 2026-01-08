# ParkingLot 
# Happy Flow --- Vehicle enters parking lot and parks the vehicle in the parkingspot

# Entities involved (ParkingLot , parkingspot,vehicle)
# Layer 1 - SkeletonFlow
# Step 1.1 — Minimal classes
class Vehicle:
    def __init__(self,vehicle_type):
        # self.registration_no=registration_no
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self,spot_id):
        self.spot_id = spot_id
        self.is_available = True
        
    def __str__(self):
        return  f'spot_id:{self.spot_id}'

# Step 1.2 — Parking Lot with One Flow

# class ParkingLot:
#     def __init__(self):
#         self.parking_spots = [ParkingSpot(i) for i in range(2)]

#     def park_a_vehicle(self,vehicle):
#         # Go through all parking spots and check if it is available
#         for parking_spot in self.parking_spots:
#             # if the spot is available then assign the vehicle to the spot
#             if parking_spot.is_available:
#                 parking_spot.is_available = False
#                 print(f"{vehicle.vehicle_type} parked at spot {parking_spot.spot_id}")
#                 return
#         print("No spot available")
        
# 🟡 LAYER 2 — State Expansion (Ticket + Exit)

# Step 2.1 — Add Ticket (NO logic)
class Ticket:
    def __init__(self,ticket_no,floor_id,spot_id):
        self.ticket_no=ticket_no
        self.spot_id = spot_id
        self.floor_id = floor_id
        
# Step 2.2 — Modify park_vehicle to return ticket
# class ParkingLot:
#     def __init__(self):
#         self.parking_spots = [ParkingSpot(i) for i in range(2)]

#     def park_a_vehicle(self,vehicle):
#         # Go through all parking spots and check if it is available
#         for index,parking_spot in enumerate(self.parking_spots):
#             # if the spot is available then assign the vehicle to the spot
#             if parking_spot.is_available:
#                 ticket=Ticket(index,parking_spot.spot_id)
#                 parking_spot.is_available = False
#                 print(f"{vehicle.vehicle_type}  parked at spot {ticket.spot_id}")
#                 return ticket
#         print("No spot available")

#     # Step 2.3 — Add exit flow
#     def exit_vehicle(self,ticket):
#         parking_spot = self.parking_spots[ticket.spot_id]
#         parking_spot.is_available = True
#         print(f"Spot {parking_spot.spot_id} freed")

#     def check_available_spots(self):
#         available_spots = list(filter(lambda X:X.is_available==True ,self.parking_spots))
#         available_spot_ids = [spot.spot_id for spot in available_spots]
#         print(available_spot_ids)
        
# 🟠 LAYER 3 — Structural Expansion (Multiple Floors)
class Floor:
    def __init__(self,floor_id):
        self.floor_id = floor_id
        self.parking_spots = [ParkingSpot(i) for i in range(2)]
        
class ParkingLot:
    def __init__(self):
        self.floors = [Floor(0),Floor(1)]

    def park_a_vehicle(self,vehicle):
        # Go through all parking spots and check if it is available
        for index,floor in enumerate(self.floors):
            # if the spot is available then assign the vehicle to the spot
            for parking_spot in floor.parking_spots:
                if parking_spot.is_available:
                    ticket=Ticket(index,floor.floor_id,parking_spot.spot_id)
                    parking_spot.is_available = False
                    print(f"{vehicle.vehicle_type}  parked at floor {ticket.floor_id} spot {ticket.spot_id}")
                    return ticket
        print("No spot available")

#     # Step 2.3 — Add exit flow
    def exit_vehicle(self,ticket):
        floor_id,spot_id = ticket.floor_id,ticket.spot_id
        parking_spot = self.floors[floor_id].parking_spots[spot_id]
        parking_spot.is_available = True
        print(f"Spot {parking_spot.spot_id} in floor {floor_id} freed")

#     def check_available_spots(self):
#         available_spots = list(filter(lambda X:X.is_available==True ,self.parking_spots))
#         available_spot_ids = [spot.spot_id for spot in available_spots]
#         print(available_spot_ids)

        
# Step 1.3 — Fake main / Client Code
parking_lot = ParkingLot()
car = Vehicle("Car")
bike = Vehicle("Bike")
meteor = Vehicle("Meteor Bike") 
altroz = Vehicle("Altroz Car")
car_ticket= parking_lot.park_a_vehicle(car)
bike_ticket = parking_lot.park_a_vehicle(bike)
meteor_ticket = parking_lot.park_a_vehicle(meteor)
altroz_ticket = parking_lot.park_a_vehicle(altroz)
parking_lot.exit_vehicle(car_ticket)
parking_lot.exit_vehicle(altroz_ticket)
# parking_lot.check_available_spots()