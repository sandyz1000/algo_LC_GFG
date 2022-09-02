"""
How to design a parking lot using object-oriented principles?

Design a parking lot using object-oriented principles.

Asked In : Amazon, Apple, Google and many more interviews

Solution: For our purposes right now, we'll make the following assumptions. We made these
specific assumptions to add a bit of complexity to the problem without adding too much. If you
made different assumptions, that's totally fine.

1) The parking lot has multiple levels. Each level has multiple rows of spots.
2) The parking lot can park motorcycles, cars, and buses.
3) The parking lot has motorcycle spots, compact spots, and large spots.
4) A motorcycle can park in any spot.
5) A car can park in either a single compact spot or a single large spot.
6) A bus can park in five large spots that are consecutive and within the same row. It cannot park
in small spots.

In the below implementation, we have created an abstract class Vehicle, from which Car, Bus,
and Motorcycle inherit. To handle the different parking spot sizes, we have just one class
ParkingSpot which has a member variable indicating the size.

"""

from abc import ABCMeta, abstractmethod


# Vehicle and its inherited classes.
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3


class Vehicle:
    __metaclass__ = ABCMeta

    parking_spots = []
    license_plate = ""
    spots_needed = 0
    size = None

    def get_spots_needed(self):
        return self.spots_needed

    def get_size(self):
        return self.size

    def parkin_spot(self, s):
        """Park vehicle in this spot (among others, potentially)"""
        self.parking_spots.append(s)

    def clear_spots(self):
        """Remove vehicle from spot, and notify spot that it's gone"""
        pass

    @abstractmethod
    def can_fitin_spot(self, spot):
        """
        Checks if the spot is big enough for the vehicle (and is available).
        This * compares the SIZE only.It does not check if it has enough spots.
        """
        pass


class Bus(Vehicle):
    def __index__(self):
        self.spots_needed = 5
        self.size = VehicleSize.Large

    def can_fitin_spot(self, spot):
        pass


class Car(Vehicle):
    def __init__(self):
        self.spots_needed = 1
        self.size = VehicleSize.Compact

    def can_fitin_spot(self, spot):
        """Checks if the spot is a Compact or a Large."""
        pass


class Motorcycle(Vehicle):
    def __init__(self):
        self.spots_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fitin_spot(self, spot):
        pass


class ParkingLot:
    """
    The ParkingLot class is essentially a wrapper class for an array of Levels. By implementing
    it this way, we are able to separate out logic that deals with actually finding free spots
    and parking cars out from the broader actions of the ParkingLot. If we didn't do it this way,
    we would need to hold parking spots in some sort of double array (or hash table which maps
    from a level number to the list of spots). It's cleaner to just separate ParkingLot from Level.
    """
    levels = []
    NUM_LEVELS = 5

    def __init__(self):
        pass

    def park_vehicle(self, vehicle):
        """Park the vehicle in a spot (or multiple spots). Return false if failed."""
        pass


class Level:
    """Represents a level in a parking garage"""

    def __init__(self, flr, number_spots):
        """
        :param flr: int
        :param number_spots: int
        """
        self.spots = []  # Represent List[ParkingSpot]
        self.floor = flr
        self.available_spots = number_spots  # number of free spots

    def park_vehicle(self, vehicle):
        """Find a place to park this vehicle. Return false if failed."""

    def park_starting_at_spot(self, num, v):
        """
        Park a vehicle starting at the spot spotNumber, and continuing until
        vehicle.spotsNeeded.
        """

    def find_available_spots(self, vehicle):
        """Find a spot to park this vehicle. Return index of spot, or -1 on failure."""

    def spot_freed(self):
        """When a car was removed from the spot, increment availableSpots"""
        self.available_spots += 1


class ParkingSpot:
    """
    The ParkingSpot is implemented by having just a variable which represents the size of the spot.
    We could have implemented this by having classes for LargeSpot, CompactSpot,
    and MotorcycleSpot which inherit from ParkingSpot, but this is probably overkilled. The spots
    probably do not have different behaviors, other than their sizes.
    """
    def __init__(self, lvl, row, spot_number, spot_size):
        """
        :param lvl: Level
        :param row: int
        :param spot_number: int
        :param spot_size: VehicleSize
        """
        self.level = lvl
        self.row = row
        self.spot_size = spot_size
        self.spot_number = spot_number
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def can_fit_vehicle(self, vehicle):
        """Check if the spot is big enough and is available"""
        pass

    def park(self, vehicle):
        """Park vehicle in this spot."""
        pass

    def remove_vehicle(self):
        """Remove vehicle from spot, and notify level that a new spot is available"""
