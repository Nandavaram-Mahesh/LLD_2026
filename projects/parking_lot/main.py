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


# Step 1.2 — Parking Lot with One Flow
class ParkingLot:
    def __init__(self):
        self.parking_spots = [ParkingSpot(i) for i in range(2)]

    def park_a_vehicle(self,vehicle):
        # Go through all parking spots and check if it is available
        for parking_spot in self.parking_spots:
            # if the spot is available then assign the vehicle to the spot
            if parking_spot.is_available:
                parking_spot.is_available = False
                print(f"{vehicle.vehicle_type} parked at spot {parking_spot.spot_id}")
                return
        print("No spot available")
    
# Step 1.3 — Fake main / Client Code
parking_lot = ParkingLot()
car = Vehicle("Car")
bike = Vehicle("Bike")
parking_lot.park_a_vehicle(car)
parking_lot.park_a_vehicle(bike)

